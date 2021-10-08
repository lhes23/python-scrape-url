import requests
from bs4 import BeautifulSoup as bs
import csv

url = 'https://onlinetrepreneur.com'
html = requests.get(url)
soup = bs(html.text,'lxml')
title = soup.find('title') 
print(title.text)

data = [[url,title.text]]

with open('scrape-url.csv','w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(data)
writeFile.close()