import boto3

# Connect to EC2
ec2 = boto3.resource('ec2')
instance_python = ''
for inst in ec2.instances.all():
    print(inst.id, inst.state, inst.public_ip_address)
    print(inst.tags)
    for tag in inst.tags:
        if(tag['Key'] == 'Name' and tag['Value'] == 'PythonDemo'):
            instance_python = inst
            break

# Terminate the instance
instance_python.terminate()