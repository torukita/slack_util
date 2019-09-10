#!/usr/bin/env python

import os
import logging
from slack_util.logging import SlackLoggingHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)

slackHandler = SlackLoggingHandler(os.environ['SLACK_WEBHOOK_URL'])
slackHandler.setLevel(logging.INFO)

logger.addHandler(slackHandler)

if __name__ == '__main__':
    logger.error('error hogehoge')
    logger.info('info hogehoge')
    logger.warning('warning hogehoge')



