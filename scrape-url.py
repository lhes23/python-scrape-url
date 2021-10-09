import requests
from bs4 import BeautifulSoup as bs
import csv

data = []

def scrapeURL(url):
    html = requests.get(url)
    soup = bs(html.text,'lxml')
    title = soup.find('title')
    data.append([url,title.text])
    return data

def writeCSV(records):
    with open('scrape-url.csv','w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(records)
    writeFile.close()

urls = (
    'https://onlinetrepreneur.com',
    'http://agreview.net'
)

for url in urls:
    records = scrapeURL(url)
    writeCSV(records)

print('Successfully Added')