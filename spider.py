from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time
import random

url="https://tw.news.yahoo.com/finance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}

headers2 = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Origin": "https://example.com",
    "Pragma": "no-cache",
    "Referer": "https://example.com/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),   
}

def parser(url):
    response = requests.get(url,headers=headers2)
    response.raise_for_status() #有異常就終止
    return BeautifulSoup(response.text)

soup = parser(url)
news_list = soup.find_all("a")
for n in news_list:
    print(f'新聞標題：{n.text}')
    delay = random.uniform(5,7.3)
    time.sleep(delay)
    subsoup = parser(n.get("href"))
    body = subsoup.body.text
    print(f'新聞內文：{body}')


