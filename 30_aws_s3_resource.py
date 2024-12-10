import boto3

# Connect to the S3 service
s3 = boto3.resource('s3')

bucketName = 'my-bucket-ashwani'
keyname = '31_aws_s3_client.py'
filename= '31_aws_s3_client.py'
saveFileToLocal = 'downloaded_file.py'

# Upload a file to S3 (key, filename) 
s3.Bucket(bucketName).upload_file(keyname,filename)

# Download a file from S3 (key, localFilename)
s3.Bucket(bucketName).download_file(keyname,saveFileToLocal)
