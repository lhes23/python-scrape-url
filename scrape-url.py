import requests
from bs4 import BeautifulSoup as bs

html = requests.get('https://onlinetrepreneur.com')
soup = bs(html.text,'lxml')
title = soup.find('title') 
print(title.text)