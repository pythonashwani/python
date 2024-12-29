import boto3

# Connect to the S3 service
s3 = boto3.resource('s3')

bucketName = 'my-bucket-ashwani'
keyname = 'requirements.txt'
filename= 'requirements.txt'
saveFileToLocal = 'downloaded_file.py'

# Upload a file to S3 (key, filename) 
s3.Bucket(bucketName).upload_file(keyname,filename)
print("File has been uploaded into the s3 bucket")


# Download a file from S3 (key, localFilename)
s3.Bucket(bucketName).download_file(keyname,saveFileToLocal)

print("File has been downloaded into local system")