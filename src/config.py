# config.py

import os
from dotenv import load_dotenv

# .env ファイルの内容を読み込む
load_dotenv()

# 設定情報を辞書として管理
CONFIG = {
    'URL': 'https://github.com/yt-hsgw/practice_repository',  # 監視対象のURL。現在はサンプルのURLを設定している
    'HASH_FILE': 'page_hash.txt',  # ハッシュ値を保存するファイル
    'LINE_NOTIFY_API': 'https://notify-api.line.me/api/notify',  # LINE NotifyのAPIエンドポイント
    'LINE_TOKEN': os.getenv('LINE_NOTIFY_TOKEN'),  # LINE Notifyのトークン
    'USER_AGENT' : os.getenv('USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
}
