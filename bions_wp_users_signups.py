import json

import boto3


def lambda_handler(event, context):
    global result
    social = event['queryStringParameters']['social']
    forgot = event['queryStringParameters']['forgot']

    tablename = 'bions_wp_user_signups'
    dynamodb_cli = boto3.client('dynamodb')

    if social == '1' and forgot == '0':
        item = {
            'user_id': {'S': event['queryStringParameters']['user_id']},
            'user_email': {'S': event['queryStringParameters']['user_email']},
            'user_login': {'S': event['queryStringParameters']['user_login']},
            'user_pass': {'S': event['queryStringParameters']['user_pass']},
            'user_nicename': {'S': event['queryStringParameters']['user_nicename']},
            'display_name': {'S': event['queryStringParameters']['display_name']},
            'nickname': {'S': event['queryStringParameters']['nickname']},
            'first_name': {'S': event['queryStringParameters']['first_name']},
            'last_name': {'S': event['queryStringParameters']['last_name']},
        }
        result = dynamodb_cli.put_item(TableName=tablename, Item=item)
    elif social == '0' and forgot == '0':
        item = {
            'user_id': {'S': event['queryStringParameters']['user_id']},
            'user_email': {'S': event['queryStringParameters']['user_email']},
            'user_login': {'S': event['queryStringParameters']['user_login']},
            'user_pass': {'S': event['queryStringParameters']['user_pass']},
        }
        result = dynamodb_cli.put_item(TableName=tablename, Item=item)
    elif social == '0' and forgot == '1':
        user_id = event['queryStringParameters']['user_id']
        user_email = event['queryStringParameters']['user_email']
        user_pass = event['queryStringParameters']['user_pass']

        from boto3.dynamodb.conditions import Attr
        dynamo_table = boto3.resource('dynamodb').Table(tablename)

        try:
            response_item = dynamo_table.scan(FilterExpression=Attr('user_id').eq(user_id))['Items']
            for it in response_item:
                if it['user_email'] == user_email:
                    result = dynamodb_cli.update_item(
                        TableName=tablename,
                        Key={
                            "user_id": {'S': user_id},
                            'user_email': {'S': user_email}
                        },
                        UpdateExpression="SET #user_pass = :pass",
                        ExpressionAttributeNames={
                            "#user_pass": "user_pass",
                        },
                        ExpressionAttributeValues={
                            ":pass": {"S": user_pass},
                        }
                    )
        except Exception as e:
            print(e)
    return {
        'statusCode': 200,
        'body': json.dumps("result: " + str(result))
    }
