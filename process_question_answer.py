import json
from datetime import datetime, timezone
from os.path import join, exists

import boto3
from fuzzywuzzy.process import extractOne

region = 'ap-south-1'
process_question_answer_table = 'process_question_answer_table'


def UpdateToDynamodb(launch_time, sub_code, question, answer, score):
    item = {
        'launch_time': {'S': str(launch_time)},
        'sub_code': {'S': sub_code},
        'question': {'S': question},
        'answer': {'S': answer},
        'score': {'S': str(score)}
    }
    dynamodb_cli = boto3.client('dynamodb')
    res = dynamodb_cli.put_item(TableName=process_question_answer_table, Item=item)


def ReturnResponse(launch_time, sub_code, question, answer, score):
    return {'launch_time': launch_time,
            'sub_code': sub_code,
            'question': question,
            'answer': answer,
            'score': score
            }


def lambda_handler(event, context):
    global row, csv_filename
    test = str(event['queryStringParameters']['t'])
    sub_code = str(event['queryStringParameters']['s']).upper()
    question = str(event['queryStringParameters']['q']).upper()
    launch_time = datetime.now(tz=timezone.utc).strftime('%y-%m-%d %H:%M:%S')
    response = {}
    csv_filename = ""
    if sub_code == "":
        response = ReturnResponse(launch_time, "", "", "", 0)
    else:
        csv_filename = join("subjects", sub_code + '.csv')

    if test == "0":  # no test
        if question == "":
            response = ReturnResponse(launch_time, sub_code, '', '', 0)
        else:
            # with open('names.csv', 'w', newline='') as csvfile:
            #     writer = csv.DictWriter(csvfile, fieldnames=['first_name', 'last_name'])
            #     writer.writeheader()
            #     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})

            question1_dict, question2_dict, answer_dict = {}, {}, {}
            with open(csv_filename, "rb") as csvfile:  # os.getcwd() == '/var/task'
                lines = csvfile.readlines()
                for i, row in enumerate(lines):
                    try:
                        line_splits = str(row).split("|")
                        # question1_dict.update({i: line_splits[1].split("b'")[-1]})
                        question1_dict.update({i: line_splits[1]})
                        question2_dict.update({i: line_splits[2]})
                        answer_dict.update({i: line_splits[3]})
                    except Exception as e:
                        print(e)
            # with open(csv_filename, newline='') as csvfile:  # os.getcwd() == '/var/task'
            #     reader = DictReader(csvfile)
            #     for i, row in enumerate(reader):
            #         question1_dict.update({i: row['question1']})
            #         question2_dict.update({i: row['question2']})
            #         answer_dict.update({i: row['answer']})

            question1_score = extractOne(question, list(question1_dict.values()))
            question2_score = extractOne(question, list(question2_dict.values()))

            if question1_score[1] > question2_score[1]:
                for i, question in enumerate(list(question1_dict.values())):
                    if question == question1_score[0]:
                        if answer_dict[i] == "":
                            response = ReturnResponse(launch_time, sub_code, question, '', question1_score[1])
                        else:
                            UpdateToDynamodb(launch_time, sub_code, question, answer_dict[i], question1_score[1])
                            response = ReturnResponse(launch_time, sub_code, question, answer_dict[i],
                                                      question1_score[1])
                        break
            else:
                for i, question in enumerate(list(question2_dict.values())):
                    if question == question2_score[0]:
                        if answer_dict[i] == "":
                            response = ReturnResponse(launch_time, sub_code, question, '', question2_score[1])
                        else:
                            UpdateToDynamodb(launch_time, sub_code, question, answer_dict[i], question2_score[1])
                            response = ReturnResponse(launch_time, sub_code, question, answer_dict[i],
                                                      question2_score[1])
                        break
    else:
        if exists(csv_filename):
            response = ReturnResponse(launch_time, sub_code, question, '', 0)
        else:
            response = ReturnResponse(launch_time, '', '', '', 0)

    # print(response)

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(response)
    }
