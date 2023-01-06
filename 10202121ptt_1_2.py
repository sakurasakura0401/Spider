import requests
from bs4 import BeautifulSoup

f = open("file.txt","w")
r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
#print(r.text)

soup = BeautifulSoup(r.text,"html.parser")
#print(soup.prettify)
sel = soup.find_all("a")

for s in sel:
    print(s["href"],s.text)
    f.write(str(s["href"]) + s.text+"\n")
f.close