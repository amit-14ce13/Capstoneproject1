import boto3

s3_client = boto3.client('s3')
s3_client.upload_file('/home/shtlp0059/Desktop/Capstoneproject1/transform.json','staging-for-load', 'dwh/vermeer/transformamit.json')