import feedparser

URL = "https://www.travelandleisure.com/rss"

def get_travel_news():
    try:
        feed = feedparser.parse(URL)

        deals = []

        for item in feed.entries[:3]:
            deals.append("• " + item.title)

        if deals:
            return "✈️ <b>Travel Updates</b>\n" + "\n".join(deals)

    except:
        pass

    return "✈️ <b>Travel Updates</b>\n• No major travel update today."
