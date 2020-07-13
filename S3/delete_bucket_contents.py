import sys

import boto3


bucket_names = []
s3 = boto3.resource('s3')
for bucket_name in bucket_names:
    bucket = s3.Bucket(bucket_name)
    for key in bucket.objects.all():
        try:
            response = key.delete()
            print(response)
        except Exception as err:
            print(err)
