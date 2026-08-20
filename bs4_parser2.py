from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://www.google.com/search?q=2330"
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

tag_a=soup.find("div",class_="VwiC3b yXK7lf p4wth r025kc Hdw6tb")
pprint(soup.text)
