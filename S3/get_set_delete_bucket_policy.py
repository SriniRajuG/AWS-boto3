import json

import boto3

# ----------------------------------
# SET a bucket policy
# ----------------------------------
bucket_name = 'BUCKET_NAME'
bucket_policy = {
    'Version': '2012-10-17',
    'Statement': [{
        'Sid': 'AddPerm',
        'Effect': 'Allow',
        'Principal': '*',
        'Action': ['s3:GetObject'],
        'Resource': f'arn:aws:s3:::{bucket_name}/*'
    }]
}

bucket_policy = json.dumps(bucket_policy)

s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)



# ----------------------------------
# DELETE a bucket policy
# ----------------------------------
s3 = boto3.client('s3')
s3.delete_bucket_policy(Bucket='BUCKET_NAME')



# ----------------------------------
# RETRIEVE a bucket policy
# ----------------------------------
s3 = boto3.client('s3')
result = s3.get_bucket_policy(Bucket='BUCKET_NAME')
print(result['Policy'])
