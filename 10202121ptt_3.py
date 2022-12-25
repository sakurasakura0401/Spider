import requests
from bs4 import BeautifulSoup

r = requests.Session()
payload ={
    "from":"/bbs/Gossiping/index.html",
    "yes":"yes"
}

r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload)
r2 = r.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(r2.text)