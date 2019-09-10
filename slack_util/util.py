import os
import logging
import json
import urllib.request

__version__ = '0.0.2'

def isJson(msg):
    try:
        json.loads(msg)
    except json.JSONDecodeError as e:
        return False
    return True

def getLogger():
    logger = logging.getLogger()
    if os.environ.get('LOG_LEVEL'):
        level = logging.getLevelName(os.environ.get('LOG_LEVEL').upper())
        if not isinstance(level, int):
            level = loggin.INFO
        logger.setLevel(level)
    return logger

def post_slack(url, slack_data):
    try:
        data_str = json.dumps(slack_data).encode('utf-8')
        request = urllib.request.Request(
            url,
            data=data_str,
            method='POST',
        )
        request.add_header('Content-Type', 'application/json')
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode('utf-8')
    except Exception as e:
        raise(e)
