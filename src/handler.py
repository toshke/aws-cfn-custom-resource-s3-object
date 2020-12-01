import json
from cr_response import CustomResourceResponse

def get_physical_id(r_properties):
  """ Generated resource id """
  bucket = r_properties['Bucket']
  key = r_properties['Key']
  return f's3://{bucket}/{key}'


def object_exists(s3_url):
  pass

def create_update_resource(props):
  pass

def delete_resource(props):
  pass

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
