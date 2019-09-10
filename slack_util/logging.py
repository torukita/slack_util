import logging
import urllib.request
import json

__version__ = '0.0.1'

class SlackLoggingHandler(logging.Handler):
    default_color = {
        logging.NOTSET: 'none',
        logging.DEBUG: 'none',
        logging.INFO: 'good',
        logging.WARNING: 'warning',
        logging.ERROR: 'danger',
        logging.CRITICAL: 'danger'
    }

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.color = self.default_color

    def _mk_slack_data(self, record):
        # print(record.__dict__)
        attachments = [ {"text": self.format(record), "color": self.color[record.levelno]} ]
        asctime = logging.Formatter().formatTime(record)
        slack_data = {
            "text": f'[{asctime}] {record.levelname}',
            "attachments": attachments,
        }
        return slack_data

    def setColor(self, color):
        self.color[logging.NOTSET] = color.get(logging.NOTSET, 'none')
        self.color[logging.DEBUG] = color.get(logging.DEBUG, 'none')
        self.color[logging.INFO] = color.get(logging.INFO, 'none')
        self.color[logging.WARNING] = color.get(logging.WARNING, 'none')
        self.color[logging.ERROR] = color.get(logging.ERROR, 'none')
        self.color[logging.CRITICAL] = color.get(logging.CRITICAL, 'none')

    def emit(self, record):
        slack_data = self._mk_slack_data(record)
        try:
            data_str = json.dumps(slack_data).encode('utf-8')
            request = urllib.request.Request(
                self.url,
                data=data_str,
                method='POST',
            )
            request.add_header('Content-Type', 'application/json')
            with urllib.request.urlopen(request) as response:
                response_body = response.read().decode('utf-8')
        except Exception as e:
            self.handleError(record)

