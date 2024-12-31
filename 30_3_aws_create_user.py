import boto3


def user_example(username):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    print(response)
    print("User has been created" , username)
    print("User ARN is: ", response['User']['Arn'])
    print("User created on: ", response['User']['CreateDate'])
    print("User Id is: ", response['User']['UserId'])
    print("User Name is: ", response['User']['UserName'])
    print("User Path is: ", response['User']['Path'])


user_example('pythonNewUser')
