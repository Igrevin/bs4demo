import requests
from pprint import pprint
from bs4 import BeautifulSoup
import os
import time
from datetime import datetime
import schedule

url = "https://api.finmindtrade.com/api/v4/data"

headers = {
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

params = {
    "dataset":"TaiwanStockInfo",
    "data_id":"2330",
    "start_date":"2026-08-20",
    "end_date":"2026-08-24"
}

response = requests.get(url,headers=headers,params=params)
response.raise_for_status() #有異常就終止
pprint(response.json())

# url = "https://httpbin.org/forms/post"   這是表單顯示的網頁   請記得不要犯這錯誤
url = "https://httpbin.org/post"  # 觀察表單內<form action="????????">
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",    
    "Pragma": "no-cache",    
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
}

#post 的資料?  params , data , json ???
data = {
    "custname": "post demo",
    "custtel": "0912-3456789"
}

response = requests.post(url=url, headers=headers, data=data)

pprint(response.status_code)
pprint(response.text)

def time_():
    print(f"現在時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

while True:
    time_()
    time.sleep(5)
