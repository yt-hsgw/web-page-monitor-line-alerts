import logging
import requests
from config import CONFIG
from logging_config import setup_logging
from utils import calculate_hash, clean_content
from notification import send_line_notification

# ログ設定
setup_logging()

def get_page_content(url):
    """指定されたURLからページコンテンツを取得する"""
    try:
        headers = {
            'User-Agent': CONFIG['USER_AGENT']
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        logging.info('Page content successfully fetched.')
        return response.text
    except requests.RequestException as e:
        logging.error(f'Error fetching page content from {url}: {e}')
        raise

def get_previous_hash():
    """以前のハッシュ値をファイルから取得する"""
    try:
        with open(CONFIG['HASH_FILE'], 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        logging.warning('Hash file not found, starting with no previous hash.')
        return ''

def save_current_hash(hash_value):
    """現在のハッシュ値をファイルに保存する"""
    try:
        with open(CONFIG['HASH_FILE'], 'w') as file:
            file.write(hash_value)
        logging.info('Current hash successfully saved.')
    except IOError as e:
        logging.error(f'Error saving current hash to {CONFIG["HASH_FILE"]}: {e}')
        raise

def check_for_updates():
    """ページの更新をチェックし、変更があれば通知を送信する"""
    logging.info('Checking for updates...')
    try:
        content = get_page_content(CONFIG['URL'])
        cleaned_content = clean_content(content)
        current_hash = calculate_hash(cleaned_content)
        previous_hash = get_previous_hash()

        if current_hash != previous_hash:
            save_current_hash(current_hash)
            send_line_notification(f'こちらのページが更新されました！\n{CONFIG["URL"]}')
            logging.info('Update detected and notification sent.')
        else:
            logging.info('No update detected.')
    except Exception as e:
        logging.error(f'Error during update check: {e}')

if __name__ == '__main__':
    check_for_updates()
