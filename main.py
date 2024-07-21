import requests
import hashlib
import os
from bs4 import BeautifulSoup

URL = 'https://zenn.dev/yt_hsgw/articles/dd00df2235e208'
HASH_FILE = 'page_hash.txt'
LINE_NOTIFY_API = 'https://notify-api.line.me/api/notify'
LINE_TOKEN = os.getenv('LINE_NOTIFY_TOKEN')

def get_page_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def calculate_hash(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def get_previous_hash():
    try:
        with open(HASH_FILE, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ''

def save_current_hash(hash_value):
    with open(HASH_FILE, 'w') as file:
        file.write(hash_value)

def send_line_notification(message):
    headers = {
        'Authorization': f'Bearer {LINE_TOKEN}',
    }
    data = {
        'message': message,
    }
    response = requests.post(LINE_NOTIFY_API, headers=headers, data=data)
    response.raise_for_status()

def check_for_updates():
    content = get_page_content(URL)
    current_hash = calculate_hash(content)
    previous_hash = get_previous_hash()

    if current_hash != previous_hash:
        save_current_hash(current_hash)
        send_line_notification(f'ページが更新されました！\n{URL}')
        print('Page updated and notification sent!')
    else:
        print('No update detected.')

if __name__ == '__main__':
    check_for_updates()
