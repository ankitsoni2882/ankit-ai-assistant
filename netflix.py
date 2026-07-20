import requests
from bs4 import BeautifulSoup

def get_netflix_updates():
    india = []
    global_list = []

    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        # India Leaving Soon
        india_url = "https://www.whats-on-netflix.com/leaving-soon/"
        r = requests.get(india_url, headers=headers, timeout=20)

        soup = BeautifulSoup(r.text, "html.parser")

        for h in soup.find_all(["h2", "h3"]):
            text = h.get_text(strip=True)

            if "India" in text:
                ul = h.find_next("ul")
                if ul:
                    for li in ul.find_all("li")[:5]:
                        india.append("• " + li.get_text(" ", strip=True))
                break

        # Global Leaving Soon
        for h in soup.find_all(["h2", "h3"]):
            text = h.get_text(strip=True)

            if "Leaving Netflix" in text:
                ul = h.find_next("ul")
                if ul:
                    for li in ul.find_all("li")[:5]:
                        global_list.append("• " + li.get_text(" ", strip=True))
                break

    except:
        pass

    message = "🎬 <b>Netflix Leaving This Month</b>\n"

    if india:
        message += "\n🇮🇳 <b>India</b>\n"
        message += "\n".join(india)
    else:
        message += "\n🇮🇳 No India list available."

    if global_list:
        message += "\n\n🌍 <b>Global</b>\n"
        message += "\n".join(global_list)

    return message
