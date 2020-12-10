import logging
from urllib.request import urlopen, Request, HTTPError, URLError
import json

logger = logging.getLogger()

class CustomResourceResponse:
    def __init__(self, event):
        self.event = event
        self.response = {
            "StackId": event["StackId"],
            "RequestId": event["RequestId"],
            "LogicalResourceId": event["LogicalResourceId"],
            "Status": 'SUCCESS',
        }
    
    def _send_response(self, resp_object):
        req_data =  json.dumps(resp_object).encode('utf-8')
        req = Request(
            self.event['ResponseURL'],
            data=req_data,
            headers={'Content-Length': len(req_data),'Content-Type': ''}
        )
        req.get_method = lambda: 'PUT'
        
        try:
            urlopen(req)
            logger.debug("Response to CFN API succeeded, nothing to do here")
        except HTTPError as e:
            logger.error("Callback to CFN API failed with status %d" % e.code)
            logger.error("Response: %s" % e.reason)
        except URLError as e:
            logger.error("Failed to reach the server - %s" % e.reason)

    def success(self, physical_id=None):
        """
        Sends success signal back to CloudFormation with given physical_id for CREATE and UPDATE requests
        """
        response = self.response
        if physical_id is not None:
            response["PhysicalResourceId"] = physical_id
        elif self.event.get("PhysicalResourceId", None):
            response["PhysicalResourceId"] = self.event["PhysicalResourceId"]
        else:
            response["PhysicalResourceId"] = self.event["LogicalResourceId"]

        logger.debug(f"Received {self.event['RequestType']} request with event: {self.event}")
        logger.info(f"Responding to {self.event['RequestType']} request with: {response}")
        self._send_response(response)
       

    def error(self, message):
        """
        Sends error signal back to CloudFormation via S3 signed url
        """
        self.response['Status'] = 'FAILED'
        self.response['Reason'] = message
        self._send_response(self.response)

 