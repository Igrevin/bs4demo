from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://Igrevin.github.io/bs4demo/apple.html"
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

tag_a=soup.div
tag_b=soup.find("div",class_="topbar")
tag_c=soup.find("p",class_="hero-copy")
pprint(f"Tag A: {tag_a.text}")
pprint(f"Tag B: {tag_b.text}")
pprint(f"Tag C: {tag_c.text}")