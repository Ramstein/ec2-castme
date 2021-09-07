from datetime import datetime, timedelta, timezone

import boto3


def TimedoutOrLessCPUUtilizedInstances(ec2_res):
    T_Instances = []
    running_instances = ec2_res.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running', ],  # ['stopped', 'terminated']
            },
            {
                "Name": 'tag:Owner',
                'Values': ['CharacterCreatorNVIDIA']
            }],
    )
    if not running_instances:
        return T_Instances

    cloudwatch_client = boto3.client('cloudwatch')

    for i, instance in enumerate(running_instances):
        now_time = datetime.now(tz=timezone.utc)
        UpTimeSec = (now_time - instance.launch_time).total_seconds()
        instanceUpTime = timedelta(seconds=UpTimeSec)
        instanceUpTime_str = str(instanceUpTime).split('.')[0]

        ec2_response = cloudwatch_client.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName='CPUUtilization',
            Dimensions=[{
                'Name': 'InstanceId',
                'Value': instance.id
            }, ],
            StartTime=now_time - timedelta(seconds=600),  # 5 minute of less CPUUtilization
            EndTime=now_time,
            Period=600,
            Statistics=['Average', ],
            Unit='Percent'
        )
        print(i + 1, ", InstanceId:", instance.id, ", instanceUpTime:", instanceUpTime_str,
              ", ec2_response['Datapoints']: ", ec2_response['Datapoints'])

        # Terminate if no datapoints recieved in 10 minutes
        if ec2_response['Datapoints'] == [] and UpTimeSec >= 600:
            T_Instances.append([instance.id, instanceUpTime_str])
            continue
        # Terminate if CPUUtilization is lesser then 6%
        for cpu in ec2_response['Datapoints']:
            if 'Average' in cpu:
                if cpu['Average'] <= 6 and UpTimeSec >= 300:
                    T_Instances.append([instance.id, instanceUpTime_str])
                    continue
        # check that UpTime for instance is more then 3600 sec or not
        if UpTimeSec >= 3600:
            T_Instances.append([instance.id, instanceUpTime_str])
    return T_Instances


def StoppedInstances(ec2_res):
    stopped_instances = ec2_res.instances.filter(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['stopped', ],
            },
            {
                "Name": 'tag:Owner',
                'Values': ['CharacterCreatorNVIDIA']
            }],
    )
    T_Instances = []
    if not stopped_instances:
        return T_Instances

    for i, instance in enumerate(stopped_instances):
        now_time = datetime.now(tz=timezone.utc)
        UpTimeSec = (now_time - instance.launch_time).total_seconds()
        instanceUpTime = timedelta(seconds=UpTimeSec)
        instanceUpTime_str = str(instanceUpTime).split('.')[0]

        print(i + 1, ", InstanceId:", instance.id, ", instanceUpTime:", instanceUpTime_str, ", Stopped Instance.")
        T_Instances.append([instance.id, instanceUpTime_str])
    return T_Instances


def lambda_handler(event, context):
    ec2_res = boto3.resource('ec2')
    TerminateInstances = []
    TerminateInstances_id = []

    instances = TimedoutOrLessCPUUtilizedInstances(ec2_res)
    for instance in instances:
        TerminateInstances.append(instance)
    instances = StoppedInstances(ec2_res)
    for instance in instances:
        TerminateInstances.append(instance)

    if TerminateInstances:
        '''Updating the values in ec2_instances dynamodb table'''
        from boto3.dynamodb.conditions import Attr

        dynamo_table = boto3.resource('dynamodb').Table('ec2_instances')
        dynamodb_cli = boto3.client('dynamodb')

        for instance in TerminateInstances:
            '''Finding the timezone value from ec2_instances table and using that to update the values'''
            try:
                result = dynamo_table.scan(FilterExpression=Attr('instance_id').eq(instance[0]))
                result = dynamodb_cli.update_item(
                    TableName='ec2_instances',
                    Key={
                        "timezone": {'S': result["Items"][0]['timezone']},
                        'instance_id': {'S': instance[0]}
                    },
                    UpdateExpression="SET #terminate = :t, #instanceUpTime = :iut",
                    ExpressionAttributeNames={
                        "#terminate": "terminate",
                        "#instanceUpTime": "instanceUpTime"
                    },
                    ExpressionAttributeValues={
                        ":t": {"N": "1"},
                        ":iut": {"S": instance[1]}
                    }
                )
                TerminateInstances_id.append(instance[0])
            except Exception as e:
                print(e)
        print("TerminateInstances: ", TerminateInstances_id)
        ec2_res.instances.filter(InstanceIds=TerminateInstances_id).terminate()
    else:
        print("No instances found to terminate")
