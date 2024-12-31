from os import path
import boto3

# Connect to EC2
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0ca9fb66e076a6e32', # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-ec2-key-pair',
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name', # Name of Instance
                    'Value': 'PythonDemo'
                },
                {
                    'Key': 'Department',
                    'Value': 'Technical',
                },
                {
                    'Key': 'Environment',
                    'Value': 'Test'
                }
            ]
        }
    ]
)

print("Instance has been created")