import requests
from datetime import datetime

TOKEN = "8775655045:AAHlm9iraKRth_U8rgriT0wYZk0dr3631DE"
CHAT_ID = "188329103"

def search_news():
    query = "울산 숙박업"
    url = f"https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"
    res = requests.get(url)
    msg_lines = []
    lines = res.text.split("<item>")
    for line in lines[1:6]:
        title = line.split("<title>")[1].split("</title>")[0]
        link = line.split("<link>")[1].split("</link>")[0]
        msg_lines.append(f"• {title}\n{link}")
    return "\n\n".join(msg_lines)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

today = datetime.now().strftime("%Y년 %m월 %d일")
news = search_news()
msg = f"🏨 울산 숙박업 뉴스 - {today}\n\n{news}"
send_telegram(msg)
