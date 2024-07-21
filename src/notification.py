# notification.py

import requests
import logging
from config import CONFIG

def send_line_notification(message):
    """LINE Notifyを使って通知を送信する"""
    if CONFIG['LINE_TOKEN'] is None:
        logging.error('LINE_NOTIFY_TOKEN environment variable not set.')
        return

    try:
        headers = {
            'Authorization': f'Bearer {CONFIG["LINE_TOKEN"]}',
        }
        data = {
            'message': message,
        }
        response = requests.post(CONFIG['LINE_NOTIFY_API'], headers=headers, data=data)
        response.raise_for_status()
        logging.info('Notification sent successfully.')
    except requests.RequestException as e:
        logging.error(f'Error sending notification: {e}')
        raise
