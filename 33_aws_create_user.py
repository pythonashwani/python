import boto3


def user_example(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)


user_example('python')