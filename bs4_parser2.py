from bs4 import BeautifulSoup
import requests
from pprint import pprint

stock="2609"
url = f"https://tw.stock.yahoo.com/quote/{stock}.TW"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
}

response = requests.get(url,headers=headers)
response.raise_for_status()
#pprint(response.text)

soup = BeautifulSoup(response.text,"html.parser")
#pprint(f"網頁標題：{soup.title.string}")
#pprint(f"網頁標題：{soup.title.text}")
#pprint(soup.text)
#print(soup.body.text)
#pprint(soup.body.text)

tag_a=soup.find("span",class_="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)")
pprint(f"{stock}當前價格：{tag_a.text}")


