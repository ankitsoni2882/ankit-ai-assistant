import feedparser

FASHION_FEEDS = [
    "https://www.vogue.com/feed/rss",
    "https://www.whowhatwear.com/rss"
]

def get_fashion_news():
    news = []

    for url in FASHION_FEEDS:
        try:
            feed = feedparser.parse(url)

            for item in feed.entries[:2]:
                news.append("• " + item.title)

        except:
            pass

    if not news:
        return "👗 <b>Fashion Trends</b>\n• No major trend today."

    return "👗 <b>Fashion Trends</b>\n" + "\n".join(news[:3])
