#alternate ways
import boto3

s3 = boto3.client('s3')
bucketName = 'my-bucket-ashwani'
keyname = 'requirements.txt'
filename= 'requirements.txt'
saveFileToLocal = 'downloaded_file.py'

# Upload a file to S3
s3.upload_file(filename, bucketName, keyname)
print("File has been uploaded into the s3 bucket")

# Download a file from S3
s3.download_file(bucketName, keyname, saveFileToLocal)
print("File has been downloaded into local system")