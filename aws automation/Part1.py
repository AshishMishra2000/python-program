import os
import boto3
s3 = boto3.resource('s3')
S3 = boto3.client('s3')

arr = os.listdir('./Upload')
for name in arr:
    location = "./Upload/"+name
    S3.upload_file(location, 'aswaumino', name)
