import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')
s3 = boto3.client('s3')
autoscaling = boto3.client('autoscaling')

print("INSTANCIAS EC2")

response = ec2.describe_instances()

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'],
              instance['InstanceType'],
              instance['State']['Name'])

print("\nBUCKETS S3")

buckets = s3.list_buckets()

for bucket in buckets['Buckets']:
    print(bucket['Name'])

print("\nAUTO SCALING")

groups = autoscaling.describe_auto_scaling_groups()

for group in groups['AutoScalingGroups']:
    print(group['AutoScalingGroupName'])
    print(group['MinSize'])
    print(group['MaxSize'])
    print(group['DesiredCapacity'])
