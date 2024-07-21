# utils.py

import hashlib
import logging
from bs4 import BeautifulSoup

def calculate_hash(content):
    """コンテンツのハッシュ値を計算する"""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def clean_content(content):
    """コンテンツをクリーンアップする"""
    try:
        soup = BeautifulSoup(content, 'html.parser')
        article = soup.find('article')
        cleaned_content = article.get_text() if article else content
        logging.info('Content successfully cleaned.')
        return cleaned_content
    except Exception as e:
        logging.error(f'Error cleaning content: {e}')
        raise
