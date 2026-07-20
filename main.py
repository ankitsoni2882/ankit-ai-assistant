import os
import requests
from news import get_news
from cars import get_car_news
from fashion import get_fashion_news
from travel import get_travel_news
from netflix import get_netflix_updates

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": msg,
            "parse_mode": "HTML",
            "disable_web_page_preview": True,
        },
        timeout=30,
    )


message = f"""
🤖 <b>Good Morning Ankit!</b>

{get_netflix_updates()}

{get_car_news()}

{get_fashion_news()}

{get_travel_news()}

{get_news()}

Have a great day! ☀️
"""

send(message)
