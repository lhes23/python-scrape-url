import requests
from bs4 import BeautifulSoup as bs

req = requests.get('https://onlinetrepreneur.com')
soup = bs(req.text,'lxml')
title = soup.find('title')
print(title.text)