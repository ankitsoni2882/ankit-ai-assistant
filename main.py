import os
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

message = """🤖 Good Morning Ankit!

✅ Your AI Assistant is now connected successfully.

This is the first test message.

Soon I'll send:
🎬 Netflix leaving soon
🚗 Car & EV news
👗 Fashion trends
✈️ Travel deals
📰 Important news

Have a great day! ☀️
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
