import feedparser

RSS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://feeds.bbci.co.uk/news/india/rss.xml",
]

def get_news():
    headlines = []

    for url in RSS:
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:2]:
                headlines.append("• " + entry.title)

        except:
            pass

    if not headlines:
        return "📰 <b>Top News</b>\n• No updates today."

    return "📰 <b>Top News</b>\n" + "\n".join(headlines[:4])
