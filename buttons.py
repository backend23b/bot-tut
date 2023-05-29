import requests

TOKEN = '6203711973:AAGcHxZWSz5rbihY3ygUdZpMZeSMxf9qSIc'
chat_id = '1258594598'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

data = {
    'chat_id': chat_id,
    'text': 'Hello world',
    'reply_markup': {
        'keyboard': [
            ['Hello', 'World'],
            ['How are you?'],
        ],
        'resize_keyboard': True
    }
}

requests.get(url=url, json=data)
