import json


def lambda_handler(event, context):
    try:
        params = event['queryStringParameters']

        a = int(params['a'])
        b = int(params['b'])

        result = a + b

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": result
            }),
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e)
            })
        }
