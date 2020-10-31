import boto3

ec2 = boto3.resource('ec2')

with open("start.sh", 'r') as f:
    script = f.read()

instances = ec2.create_instances(ImageId='ami-07db4adf15d7719d1', InstanceType='t2.micro',
                                 KeyName='aws_sem5', UserData=script, SecurityGroups=['boto_instances'], MinCount=1, MaxCount=1)

instance = instances[0]

instance.wait_until_running()
instance.load()
print("Public DNS (IPv4): " + instance.public_dns_name)
