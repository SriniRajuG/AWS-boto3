import sys

import boto3


db_name = ''  # <-------------- Fill this value
rds = boto3.client('rds')
try:
    response = rds.delete_db_instance(
        DBInstanceIdentifier=db_name,
        SkipFinalSnapshot=True
    )
    print(response)
except Exception as err:
    print(error)
