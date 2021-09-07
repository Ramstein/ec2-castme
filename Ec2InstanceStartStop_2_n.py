import json
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Attr

region = 'ap-south-1'


def sendEmail(terminate="", user_email="", user_firstname="", instance_id="", public_dns_name="", instanceUpTime_str="",
              UpTimeSec=0, launch_time='', timezone='', gender=''):
    ses_client = boto3.client('ses')
    charge = "{:.2f}".format(round(UpTimeSec * 0.000275, 2))
    UpTimeSec = int(UpTimeSec)

    if terminate == "1":
        body = ("""<p>Hi {},<br/><br/>
Your remote desktop having,<br/>
Public DNS Name: {},<br/>
Instance ID: {},<br/>
Launch Time: {} {},<br/>
Sexuality: {}, have got terminated after {} of uptime. We hope that your experience with our remote desktop character creation was smoother. If you have successfully created your character then upload it.<br/><br/>

For {} of uptime, your charges for using a remote desktop are the following.<br/>
Time spent: {} = {} seconds<br/>
Charges per hour: $0.99<br/>
Total payable charge: ${}<br/>
You can make the payment here: https://castme.life<br/><br/>

For any queries, you can reply to this email and we will get back to you as soon as possible.<br/><br/>

Thanks<br/>
https://castme.life<br/>
support@castme.life<br/>
+19562157882
</p>""").format(user_firstname, public_dns_name, instance_id, launch_time, timezone, gender, instanceUpTime_str,
                instanceUpTime_str, instanceUpTime_str, UpTimeSec, charge)
        try:
            ses_client.send_email(
                Source="support@castme.life",
                Destination={
                    'ToAddresses': [user_email],
                },
                ReplyToAddresses=['support@castme.life'],
                Message={
                    'Subject': {
                        'Data': 'Remote Desktop {} Terminated, castme.life'.format(public_dns_name),
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

    elif terminate == "0":
        body = ("""
<p>Hi {},<br/><br/>
You have launched a Digital Identity Creator Remote Desktop having,<br/>
Public DNS Name: {},<br/>
Sexuality: {},<br/>
Password: Ed;xRnObgcX.JmWp?fUm%efyr$iaIfoB<br/>
Instance ID: {}, at {} {}.<br/>
Wait for 45 sec and login to the remote desktop as documented.<br/><br/>
 
We are sure that you have watched our demo videos of creating your digital identity already multiple times, so now this is performance time. Utilize every minute smartly. Use 2k or 4k studio quality photos for creating your digital identity. After creating the character, upload it.<br/><br/>
 
Warning: This remote desktop will only last for 60 minutes from launch time so create your character within this time or save your created character file to a drive at the 55th minute. Within these 60 minutes, if you are leaving the desktop to be running or in a certain situation where CPU usage will drop less then 6 %, in this case too, your remote desktop will get terminated and there will be no any backup of your work, so backup yourself at the right time if required.<br/><br/>
 
For any queries, you can reply to this email and we will get back to you as soon as possible.<br/><br/>
 
Thanks<br/>
https://castme.life<br/>
support@castme.life<br/>
+19562157882
</p>""").format(user_firstname, public_dns_name, gender, instance_id, launch_time, timezone)
        try:
            ses_client.send_email(
                Source="support@castme.life",
                Destination={
                    'ToAddresses': [user_email],
                },
                ReplyToAddresses=['support@castme.life'],
                Message={
                    'Subject': {
                        'Data': 'Remote Desktop {} Launched, castme.life'.format(public_dns_name),
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


def start_instance(ec2_client, ec2_resource):
    timestamp = str(datetime.now()).split('.')[0]
    ec2_client.create_key_pair(KeyName='CC_KP_' + timestamp)

    instance = ec2_resource.create_instances(
        ImageId="ami-0b321c328ae76f3f4",  # Free Tier  #pass: lb;HUdWNb$3T9i(&cW5KSKB5Dck4ACAY
        InstanceType='t2.micro',  # Free Tier
        # ImageId="ami-06fd51623f25529e2",  # Nvidia Gaming PC, Windows Server 2019, 4vcpu, 16gbRam, 22.2gbGPU Tesla,
        # InstanceType="g4dn.xlarge",  # Nvidia Gaming PC, Windows Server 2019, 4vcpu, 16gbRam, 22.2gbGPU Tesla,
        MaxCount=1,
        MinCount=1,
        KeyName='CC_KP_' + timestamp,
        SecurityGroupIds=["sg-0494ddedbe286d263",  # group_info['GroupId'],
                          ],
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{
                'Key': 'Owner',
                'Value': 'CharacterCreatorNVIDIA'
            }, ]},
        ], )[0]
    # set_alarm(timestamp, instanceID=instance.id)
    instance.wait_until_running(WaiterConfig={'Delay': 2})
    instance.reload()
    return instance.id, instance.public_dns_name, instance.launch_time


def set_alarm(instanceID):
    cloudwatch = boto3.client('cloudwatch')
    account_id = str(121705095421)
    # Create alarm with actions enabled, # 'arn:aws:swf:'+region+':'+account_id+':action/actions/AWS_EC2.InstanceId.Terminate/1.0'
    alarm_action = 'arn:aws:swf:' + region + ':' + account_id + ':action/actions/AWS_EC2.InstanceId.Terminate/1.0'
    cloudwatch.put_metric_alarm(
        AlarmName='CC_A_' + instanceID,
        ComparisonOperator='LessThanThreshold',  # LessThanThreshold, LessThanOrEqualToThreshold,
        TreatMissingData='breaching',  # notBreaching, breaching, ignore, missing
        DatapointsToAlarm=2,  # 1 alarm in 3 minutes
        EvaluationPeriods=3,
        Period=300,
        Threshold=2,
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Statistic='Average',
        ActionsEnabled=True,
        AlarmActions=[alarm_action],
        AlarmDescription='Alarm when server CPU falls 2%',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instanceID
            },
        ],
        Unit='Seconds'
    )


def lambda_handler(event, context):
    terminate = event['queryStringParameters']['terminate']
    user_login = event['queryStringParameters']['user_login']
    user_email = event['queryStringParameters']['user_email']
    timezone = event['queryStringParameters']['timezone']

    response = {}
    # check that all the values provided are perfect.
    if terminate == "":
        response = {'instance_id': "", 'public_dns_name': "", 'terminate': "0", }
    elif user_login == "":
        response = {'instance_id': "", 'public_dns_name': "", 'terminate': "0", }
    elif user_email == "":
        response = {'instance_id': "", 'public_dns_name': "", 'terminate': "0", }
    elif timezone == "":
        response = {'instance_id': "", 'public_dns_name': "", 'terminate': "0", }
    else:
        global res
        ec2_resource = boto3.resource("ec2", region_name=region)
        dynamo_table = boto3.resource('dynamodb').Table('ec2_instances')
        dynamodb_cli = boto3.client('dynamodb')

        if terminate == "1":  # terminating the instances
            response_table = dynamo_table.scan(
                FilterExpression=Attr('user_login').eq(user_login) & Attr('user_email').eq(user_email) & Attr(
                    'timezone').eq(timezone) & Attr('terminate').eq(0)
            )
            if not response_table['Items']:
                response = {
                    'instance_id': "",
                    'public_dns_name': "",
                    'terminate': "0",
                }

            else:
                instance_ids2 = []
                UpTimeSec = 0
                instanceUpTime_str = ""
                for res in response_table['Items']:
                    instance_ids2.append(res['instance_id'])

                    instance = ec2_resource.instances.filter(
                        Filters=[
                            {
                                'Name': 'instance-id',
                                'Values': [res['instance_id']],
                            },
                            {
                                "Name": 'tag:Owner',
                                'Values': ['CharacterCreatorNVIDIA']
                            }],
                    )
                    if not instance:
                        continue
                    for i in instance:
                        from datetime import timezone, timedelta
                        now_time = datetime.now(tz=timezone.utc)
                        UpTimeSec = (now_time - i.launch_time).total_seconds()
                        instanceUpTime_str = str(timedelta(seconds=UpTimeSec)).split('.')[0]

                    result = dynamodb_cli.update_item(
                        TableName='ec2_instances',
                        Key={
                            "timezone": {'S': res['timezone']},
                            'instance_id': {'S': res['instance_id']}
                        },
                        UpdateExpression="SET #terminate = :t, #instanceUpTime = :tt",
                        ExpressionAttributeNames={
                            "#terminate": "terminate",
                            "#instanceUpTime": "instanceUpTime"
                        },
                        ExpressionAttributeValues={
                            ":t": {"N": "1"},
                            ":tt": {"S": instanceUpTime_str}
                        }
                    )
                if instance_ids2:
                    ec2_resource.instances.filter(InstanceIds=instance_ids2).terminate()
                    print("success updated value. ec2_instance: " + res['instance_id'] + "  " + res["public_dns_name"])

                    sendEmail(terminate=terminate, user_email=user_email, user_firstname=user_login,
                              instance_id=res['instance_id'], public_dns_name=res["public_dns_name"],
                              instanceUpTime_str=instanceUpTime_str, UpTimeSec=UpTimeSec,
                              launch_time=res['launch_time'], timezone=res['timezone'], gender=res['gender'])
                    response = {
                        'instance_id': res['instance_id'],
                        'public_dns_name': res["public_dns_name"],
                        'terminate': "1",
                    }

        elif terminate == "0":  # 0: false - starting the instances
            gender = event['queryStringParameters']['gender']  # query the gender value only if starting the instances
            if gender == "":
                response = {'instance_id': "", 'public_dns_name': "", 'terminate': "0", }
            else:
                instance_ids = [""]
                ec2_client = boto3.client('ec2', region_name=region)
                instance_ids[0], public_dns_name, launch_time = start_instance(ec2_client, ec2_resource)
                launch_time = launch_time.strftime('%y-%m-%d %H:%M:%S')
                item = {
                    'timezone': {'S': timezone},
                    'terminate': {'N': "0"},
                    'user_login': {'S': user_login},
                    'user_email': {'S': user_email},
                    'gender': {'S': gender},
                    'instance_id': {'S': instance_ids[0]},
                    'public_dns_name': {'S': public_dns_name},
                    'launch_time': {'S': str(launch_time)},
                    'instanceUpTime': {'S': ""}
                }
                res = dynamodb_cli.put_item(TableName='ec2_instances', Item=item)
                # if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
                sendEmail(terminate=terminate, user_email=user_email, user_firstname=user_login,
                          instance_id=instance_ids[0],
                          public_dns_name=public_dns_name, launch_time=launch_time, timezone=timezone, gender=gender)
                print("Updated value. ec2_instance: ", instance_ids[0], public_dns_name, "launch_time:", launch_time)
                response = {
                    'instance_id': instance_ids[0],
                    'public_dns_name': public_dns_name,
                    'terminate': "0",
                }

    return {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps(response)
    }
