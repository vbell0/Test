import time
import requests

from app.settings import SLACK_TOKEN, SLACK_URL_SERVICE
from app.logger import logger


class Slack:
    """
    Slack Message Class API
    """
    SUCCESS_COLOR = "#36a64f"
    WARNING_COLOR = "#ffcc00"
    FAIL_COLOR = "#ff0000"

    def __init__(self, robot_name, robot_icon, channel_log=None, channel_error=None):
        self.robot_name = robot_name
        self.robot_icon = robot_icon
        self.slack_channel_log = channel_log
        self.slack_channel_error = channel_error

        if not self.slack_channel_log:
            self.slack_channel_log = "#dev_teste"

        if not self.slack_channel_error:
            self.slack_channel_error = "#dev_teste"

    def send_fail_message(self, text) -> requests.Response:
        return self.send_post(self.FAIL_COLOR, text, self.slack_channel_error)

    def send_warning_message(self, text, icon=None) -> requests.Response:
        return self.send_post(self.WARNING_COLOR, text, self.slack_channel_error, icon=icon)

    def send_success_message(self, text) -> requests.Response:
        return self.send_post(self.SUCCESS_COLOR, text, self.slack_channel_log)

    def send_post(self, color, text, channel, icon=None) -> requests.Response:
        try:
            logger.info(message=text)
            _icon = icon or self.robot_icon
            _name = self.robot_name
            _channel = channel

            headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {SLACK_TOKEN}'}

            body = {
                "channel": f"{_channel}",
                "username": f"{_name}",
                "icon_emoji": f"{_icon}",
                "attachments": [
                    {
                        "color": f"{color}",
                        "text": f"{text}",
                        "ts": time.time()
                    }
                ]
            }

            response = requests.post(url=SLACK_URL_SERVICE, headers=headers, json=body)
            return response
        except Exception as error:
            logger.error(message="Erro Slack request Post", data=error, status_code=500)


if __name__ == '__main__':
    s = Slack("Integracao", ":sunglasses:")
    s.send_fail_message("ops")
