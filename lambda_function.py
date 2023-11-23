import requests
import json
import boto3

from appsync import get_subs
client = boto3.client('sns')

def lambda_handler(event, context):
    # Query for todays subs
    subs = get_subs()

    # Parse them out and push to SNS
    for sub in subs:
        print(type(json.dumps(sub)))
        response = client.publish(TopicArn="arn:aws:sns:us-east-1:571104494346:parking-sub", 
                                  Message=json.dumps(sub))
        print(response)
        


lambda_handler(None, None)