from pprint import pprint
import boto3

s3 = boto3.resource('s3')

print('S3 Buckets\n')
for bucket in s3.buckets.all():
    pprint(bucket)

ec2 = boto3.resource('ec2')

print('EC2 Instances\n')
for ins in ec2.instances.all():
    pprint(ins)

print('EC2 Instances (id, state)\n')
for ins in ec2.instances.all():
    print(ins.id, ins.state)