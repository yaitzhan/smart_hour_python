"""
Скрипт для отправки сообщений в Telegram канал

Смартчас "Знакомство с Python"

Предварительно необходимо:
    1. создать бота в Telegram, скопировать токен
    2. создать Telegram канал
    3. добавить бота в канал в качестве админа
    4. скопировать токен бота в BOT_TOKEN
    5. скопировать id канала в CHANNEL_ID:
        а. как найти id Telegram канала: https://github.com/GabrielRF/telegram-id#web-channel-id

"""
import requests


BOT_TOKEN = ''
CHANNEL_ID = ''


def send_to_channel(text):
    """
    Делает POST запрос для отправки сообщения в Telegram канал

    :param text: текст сообщения
    """
    payload = {
        'chat_id': f'{CHANNEL_ID}',
        'text': text
    }
    requests.post(f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage', json=payload)


if __name__ == '__main__':
    msg = 'фыв'  # можно поменять текст
    send_to_channel(msg)
