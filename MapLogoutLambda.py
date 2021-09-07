import json

import boto3

region = 'ap-south-1'


def RunCommand(instance_id):
    ssm_client = boto3.client('ssm')
    response = ssm_client.send_command(
        InstanceIds=[instance_id],
        DocumentName="AWS-RunPowerShellScript",
        DocumentVersion="$LATEST",
        TimeoutSeconds=30,  # valid range 30-inf
        MaxConcurrency='50',
        MaxErrors='0',
        Parameters={'commands':
                        ['dir',
                         r'cd C:\Users\Administrator\Desktop',
                         r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe MapLogout.py',
                         'curl https://www.helenanderson.co.nz/wp-content/uploads/2019/04/ec2.png -o picture.png']},
    )
    command_id = response['Command']['CommandId']
    import time
    while 1:
        time.sleep(2)
        output = ssm_client.get_command_invocation(
            CommandId=command_id,
            InstanceId=instance_id,
        )
        if output['Status'] == "Success":
            print(output)
            return True


def lambda_handler(event, context):
    MapName = event['queryStringParameters']['MapName']
    ID = event['queryStringParameters']['ID']

    response = {}
    if MapName == "":
        response = {'success': "Map Name is not valid"}
    elif ID == "":
        response = {'success': "Login first, and create your character."}
    else:
        map_instance = {
            "Map1": "i-0dd8bd3418a66575a",
            "Map2": "i-0dd8bd3418a665j75a",
            "Map3": "i-0dd8bd3418a6huyg6575a",
            "Map4": "i-0dd8bd3418ha66575a",
        }
        if RunCommand(instance_id=map_instance[str(MapName)]):

            from datetime import datetime, timezone
            from boto3.dynamodb.conditions import Attr

            now_time = datetime.now(tz=timezone.utc).strftime('%y-%m-%d %H:%M:%S')
            dynamodb_cli = boto3.client('dynamodb')
            dynamo_table = boto3.resource('dynamodb').Table(MapName)
            result = dynamo_table.scan(
                FilterExpression=Attr('ID').eq(ID) & Attr('LoggedIn').eq(str(1))
            )
            print(result)

            result = dynamodb_cli.update_item(
                TableName=MapName,
                Key={
                    # "timezone": {'S': res['timezone']},
                    # 'instance_id': {'S': res['instance_id']}
                },
                UpdateExpression="SET #LoggedIn = :LI, #LogoutTime = :LT",
                ExpressionAttributeNames={
                    "#LoggedIn": "LoggedIn",
                    "#LogoutTime": "LogoutTime"
                },
                ExpressionAttributeValues={
                    ":LI": {"N": "0"},
                    ":LT": {"S": str(now_time)}
                }
            )
            response = {'success': "1"}
        else:
            response = {'success': "Character Mesh Setup failing."}

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(response)
    }
