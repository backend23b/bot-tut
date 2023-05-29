import requests

TOKEN = '6203711973:AAGcHxZWSz5rbihY3ygUdZpMZeSMxf9qSIc'
chat_id = '1258594598'


url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


btn1 = {'text': '12'}
btn2 = {'text': '13'}
btn3 = {'text': 'Home'}


data = {
    'chat_id': chat_id,
    'text': 'Hello world',
    'reply_markup': {
        'keyboard': [
            [btn1, btn2],
            [btn3],
        ],
        'resize_keyboard': True
    }
}

requests.get(url=url, json=data)
