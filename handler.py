import json
import os

def hello(event, context):
    body = {
        "message": 'Go Serverless v1.0! Your function executed successfully in the newest version!!!!!!!!',
        "message_var": f"{os.environ['message']}",
        # "secret": f"{os.environ['secret']}",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
