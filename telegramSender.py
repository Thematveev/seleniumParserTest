import requests

class TelegramSender:
    def __init__(self, token):
        self.token = token

    def sendMessage(self, chat_id, text):
        link = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(link)

