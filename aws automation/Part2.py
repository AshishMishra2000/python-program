import json
import boto3

session = boto3.Session()
s3 = boto3.resource('s3')
bucket = s3.Bucket('aswaumino')


for files in bucket.objects.all():
    location = "./Downloads/"+str(files.key)
    print(files.key)
    bucket.download_file(files.key, location)
