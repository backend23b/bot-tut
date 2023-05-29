import requests

TOKEN = '6203711973:AAGcHxZWSz5rbihY3ygUdZpMZeSMxf9qSIc'
chat_id = '1258594598'


url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


btn_location = {
    'text': '📍',
    'request_location': True
}
btn_contact = {
    'text': '📞',
    'request_contact': True
}


data = {
    'chat_id': chat_id,
    'text': 'send your location',
    'reply_markup': {
        'keyboard': [
            [btn_location, btn_contact]
        ],
        'resize_keyboard': True
    }
}

requests.get(url=url, json=data)
