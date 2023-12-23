import boto3

dynamo_client  =  boto3.resource(service_name = 'dynamodb',region_name = 'us-east-1')
### getting the product table
product_table = dynamo_client.Table('users')
print('getting the product table: - ',product_table.table_status)