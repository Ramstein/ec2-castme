import json

import boto3


def sendEmail(user_email, user_firstname):
    ses_client = boto3.client('ses')
    body = ("""<p>Hi {},<br/><br/>
you have successfully uploaded your character.<br/>
Thanks for making this far. Your character will be preprocessed with our automated system before it will be available to you for exploring any map. We will notify you on processing complete via an email notification. It usually takes 24 hours. Wait till that time and watch our trailers of different maps.<br/><br/>
Thanks<br/>
https://castme.life<br/>
support@castme.life<br/>
+19562157882
</p>""").format(user_firstname)

    try:
        ses_client.send_email(
            Source="support@castme.life",
            Destination={
                'ToAddresses': [user_email],
                # 'CcAddresses': [], // don't put them here if they are empty
                # 'BccAddresses': [],
            },
            ReplyToAddresses=['support@castme.life'],
            Message={
                'Subject': {
                    'Data': 'Character Upload successful, castme.life',
                    'Charset': 'utf-8'
                },
                'Body': {
                    'Text': {'Data': body, 'Charset': 'utf-8'},
                    'Html': {'Data': body, 'Charset': 'utf-8'}
                }
            }
        )
        print("email send to {}".format(user_email))
    except Exception as e:
        print(e)


def lambda_handler(event, context):
    s3_user_character_filename = event['queryStringParameters']['s3_user_character_filename']
    ID = event['queryStringParameters']['ID']
    user_email = event['queryStringParameters']['user_email']
    user_firstname = event['queryStringParameters']['user_firstname']

    response = {}
    if not s3_user_character_filename:
        response['success'] = "0"
    elif ID == "":
        response['success'] = "0"
    elif user_email == "":
        response['success'] = "0"
    else:
        from datetime import datetime, timezone

        now_time = datetime.now(tz=timezone.utc).strftime('%y-%m-%d %H:%M:%S')
        dynamodb_cli = boto3.client('dynamodb')
        res = dynamodb_cli.put_item(TableName='CharacterMeshUpload_Not_Preprocessed',
                                    Item={
                                        'filename': {'S': s3_user_character_filename},
                                        'ID': {'N': str(ID)},
                                        'user_email': {'S': user_email},
                                        'user_firstname': {'S': user_firstname},
                                        'UploadTime': {'S': str(now_time)},
                                    })
        sendEmail(user_email, user_firstname)
        response['success'] = "1"
        print("response['success'] = '1'")
    responseObject = {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(response)
    }
    return responseObject
