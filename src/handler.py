import json
import base64
from cr_response import CustomResourceResponse
import boto3

def get_physical_id(r_properties):
  """ Generated resource id """
  bucket = r_properties['Bucket']
  key = r_properties['Key']
  return f's3://{bucket}/{key}'



def create_update_resource(props):
  bucket = props['Bucket']
  key = props['Key']
  content = props['Content']
  if props.get('ContentBase64', False):
    content = base64.decodebytes(content.encode('utf-8'))
  api_arguments = {
    'Bucket':bucket,
    'Key':key,
    'Body':content.encode('utf-8'),
  }
  if 'SSE' in props:
    api_arguments['ServerSideEncryption'] = props['SSE']
  if 'SSEKmsKeyId' in props:
    api_arguments['SSEKMSKeyId'] = props['SSEKmsKeyId']
  if 'BucketKeyEnabled' in props:
    api_arguments['BucketKeyEnabled'] = props['BucketKeyEnabled']
  if 'StorageClass' in props:
    api_arguments['StorageClass'] = props['StorageClass']
  if 'ACL' in props:
    api_arguments['ACL'] = props['ACL']
  
  boto3.client('s3').put_object(**api_arguments)



def delete_resource(props):
  bucket = props['Bucket']
  key = props['Key']
  boto3.client('s3').delete_object(Bucket=bucket, Key=key)

def cr_handler(event, context):
    """
    Create, Update or Remove S3 object
    as Custom Resource for AWS CloudFormation
    """
    print(json.dumps(event))
    cfn_response = CustomResourceResponse(event)
    cfn_signal = event.get('RequestType', None)
    properties = event.get('ResourceProperties', None)
    if not cfn_signal or not properties:
      print('Payload not a valid CFN CR request object')
      return 

    try:
      if cfn_signal == 'CREATE' or cfn_signal == 'UPDATE':
        create_update_resource(properties)
      if cfn_signal == 'DELETE':
        delete_resource(properties)
      
    except Exception as e:
      cfn_response.error(str(e))
