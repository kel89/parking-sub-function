import requests
import json
import boto3

from appsync import get_subs

def lambda_handler(event, context):
    print(event)

    client = boto3.client('sns')
    # Query for todays subs
    subs = get_subs()
    print(subs)

    # Parse them out and push to SNS
    for sub in subs:
        print(json.dumps(sub))
        response = client.publish(TopicArn="arn:aws:sns:us-east-1:571104494346:parking-sub", 
                                  Message=json.dumps(sub))
        
