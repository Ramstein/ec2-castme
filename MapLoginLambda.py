import json

import boto3

region = 'ap-south-1'


def isInstanceRunning(tag_value, instance_id):
    ec2_res = boto3.resource('ec2')
    running_instances = ec2_res.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running', ],  # ['stopped', 'terminated']
            },
            {
                "Name": 'tag:Owner',
                'Values': [tag_value]
            }],
    )
    if running_instances:
        for instance in running_instances:
            if instance.id == instance_id:
                return True
    else:
        return False


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
                         r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\python.exe MapLogin.py',
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
        if isInstanceRunning(tag_value=MapName, instance_id=map_instance[str(MapName)]):
            if RunCommand(instance_id=map_instance[str(MapName)]):
                user_login = event['queryStringParameters']['user_login']
                user_email = event['queryStringParameters']['user_email']
                user_firstname = event['queryStringParameters']['user_firstname']
                user_lastname = event['queryStringParameters']['user_lastname']
                display_name = event['queryStringParameters']['display_name']
                time_zone = event['queryStringParameters']['timezone']

                from datetime import datetime, timezone
                now_time = datetime.now(tz=timezone.utc).strftime('%y-%m-%d %H:%M:%S')

                dynamodb_cli = boto3.client('dynamodb')
                res = dynamodb_cli.put_item(
                    TableName=MapName,
                    Item={
                        'ID': {'N': ID},
                        'user_login': {'S': user_login},
                        'user_email': {'S': user_email},
                        'user_firstname': {'S': user_firstname},
                        'user_lastname': {'S': user_lastname},
                        'display_name': {'S': display_name},
                        'timezone': {'S': time_zone},
                        'LoggedIn': {'N': str(1)},
                        'LoginTime': {'S': str(now_time)},
                        'LogoutTime': {'S': str(now_time)},
                    })
                response = {'success': "1"}
            else:
                response = {'success': "Character Mesh Setup failing."}
        else:
            response = {'success': "Game Map is not live."}

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(response)
    }
