import requests
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# LINEのチャネルアクセストークン (GitHub Secrets から取得)
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

# 送信するYouTube動画リスト
YOUTUBE_VIDEOS = [
    "https://youtu.be/xg74DLTw7ts",
    "https://youtu.be/RALLbdunkCQ",
]

def send_line_message():
    """LINEにYouTube動画のリンクを送信"""
    message = "📢 今日のトレーニング動画 🎥\n" + "\n".join(YOUTUBE_VIDEOS)

    url = "https://api.line.me/v2/bot/message/broadcast"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}"
    }
    data = {
        "messages": [{"type": "text", "text": message}]
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        print("メッセージ送信成功")
    else:
        print(f"送信失敗: {response.text}")

if __name__ == "__main__":
    send_line_message()