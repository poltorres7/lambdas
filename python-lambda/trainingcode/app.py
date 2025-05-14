import boto3
import json
from botocore.exceptions import ClientError


def lambda_handler(event, context):
	rds_secret = get_secret("devops-test-secret")
	host2 = rds_secret["host"]

	message = {
		"status": 200,
		"message": "Hello",
		"host": host2
	}
	return message

def get_secret(secret_name):
	client = boto3.client("secretsmanager")
	try:
		response = client.get_secret_value(SecretId=secret_name)
		print("Response: ", response)
		secret = json.loads(response["SecretString"])
		print("Secret: ", secret)
		return secret
	except ClientError as e:
		raise e
	return secret
