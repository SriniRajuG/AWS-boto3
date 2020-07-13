import boto3

s3 = boto3.client('s3')
result = s3.get_bucket_acl(Bucket='my-bucket')
print(result)
