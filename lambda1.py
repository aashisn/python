from __future__ import print_function

import boto3
import json
import logging
import os

from urllib2 import Request, urlopen, URLError, HTTPError

SLACK_CHANNEL = "#general"
HOOK_URL = "https://hooks.slack.com/services/XXXXXXXXXXXXX"
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    detail_type =  str(event['detail-type'])
    
    if detail_type == "AWS API Call via CloudTrail":
        detail_type =  str(event['detail-type'])
        some_id = str(event['id'])
    
        slack_message = {
            'channel': SLACK_CHANNEL,
            'text': "%s for ARN %s" % (detail_type, some_id)
        }
    else:
        slack_message = {
            'channel': SLACK_CHANNEL,
            'text': 'test message'
        }
        logger.info(str(slack_message))
    
        req = Request(HOOK_URL, json.dumps(slack_message))
        try:
            response = urlopen(req)
            response.read()
            logger.info("Message posted to %s", slack_message['channel'])
        except HTTPError as e:
            logger.error("Request failed: %d %s", e.code, e.reason)
        except URLError as e:
            logger.error("Server connection failed: %s", e.reason)
        else:
            logger.info("Something went wrong")