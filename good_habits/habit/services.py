import os
import requests

from ..settings import TELEGRAM_TOKEN


class MyBot():
    URL = 'https://api.telegram.org/bot'
    TOKEN = TELEGRAM_TOKEN

    def send_message(self, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': '742481601',
                'text': text,
            }
        )
