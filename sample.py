#!/usr/bin/env python

import os
import logging
from slack_util.logging import SlackLoggingHandler
import slack_util.util as util 

logger = logging.getLogger()
logger.setLevel(logging.INFO)

slackHandler = SlackLoggingHandler(os.environ['SLACK_WEBHOOK_URL'])
slackHandler.setLevel(logging.INFO)

logger.addHandler(slackHandler)

if __name__ == '__main__':
    logger.error('error hogehoge')
    logger.info('info hogehoge')
    logger.warning('warning hogehoge')

    slack_data = {
        "text": "sample text",
        "attachments": [
            {"text": "attachment text", "color": "good"}
        ]
    }
    util.post_slack(os.environ['SLACK_WEBHOOK_URL'], slack_data)

