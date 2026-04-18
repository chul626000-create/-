import requests
from datetime import datetime

TOKEN = "8775655045:AAHlm9iraKRth_U8rgriT0wYZk0dr3631DE"
CHAT_ID = "188329103"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
    print(r.status_code, r.text)

def search_news():
    query = "울산+숙박업"
    url = f"https://news.google.com/rss/search?q={query}&hl=ko&gl=KR&ceid=KR:ko"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    print("RSS 상태:", res.status_code)
    items = []
    for item in res.text.split("<item>")[1:6]:
        try:
            title = item.split("<title>")[1].split("</title>")[0]
            title = title.replace("<![CDATA[","").replace("]]>","")
            items.append(f"• {title}")
        except:
            pass
    return "\n\n".join(items) if items else "뉴스 없음"

today = datetime.now().strftime("%Y년 %m월 %d일")
news = search_news()
msg = f"🏨 울산 숙박업 뉴스 - {today}\n\n{news}"
print("보낼 메시지:", msg)
send_telegram(msg)
