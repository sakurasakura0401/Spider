import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
#print(r.text)

soup = BeautifulSoup(r.text,"html.parser")
#print(soup.prettify)
for link in soup.find_all("a"):
    print(link.get("href"))