import feedparser

URL = "https://www.autocarindia.com/rss"

def get_car_news():
    try:
        feed = feedparser.parse(URL)

        news = []

        for item in feed.entries[:3]:
            news.append("• " + item.title)

        if news:
            return "🚗 <b>Car & EV News</b>\n" + "\n".join(news)

    except:
        pass

    return "🚗 <b>Car & EV News</b>\n• No major update today."
