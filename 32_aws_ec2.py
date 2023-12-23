from os import path
import boto3

# Connect to EC2
ec2 = boto3.resource('ec2')

# Launch an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0', # Amazon Linux 2 LTS
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='my-ec2-key-pair'
)

# Get the instance ID
instance_id = instance[0].id

# Wait for the instance to be running
instance[0].wait_until_running()

# Get the instance object
instance = ec2.Instance(instance_id)

# Run a command on the instance
response = instance.execute_command(
    DocumentName='AWS-RunShellScript',
    Parameters={'commands': ['echo "Hello from EC2!"']}
)

# Get the output from the command
output = response['StandardOutputContent']

# Print the output
print(output)

# Terminate the instance
instance.terminate()