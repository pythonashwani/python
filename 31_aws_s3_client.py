#alternate ways
import boto3

s3 = boto3.client('s3')
bucketName = 'my-bucket-ashwani'
keyname = '31_aws_s3_client.py'
filename= '31_aws_s3_client.py'
saveFileToLocal = 'downloaded_file.py'

# Upload a file to S3
s3.upload_file(filename, bucketName, keyname)

# Download a file from S3
s3.download_file(bucketName, keyname, saveFileToLocal)