#alternate ways
import boto3

s3 = boto3.client('s3')
response  = s3.list_buckets()
#print(response)
print(response["Buckets"])
for i in response["Buckets"]:
    print(i["Name"])