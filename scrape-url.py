import requests
from bs4 import BeautifulSoup as bs
import csv

def scrapeURL(url):
    html = requests.get(url)
    soup = bs(html.text,'lxml')
    title = soup.find('title')
    data = []
    data.append([url,title.text])
    return data

def writeCSV(data):
    with open('scrape-url.csv','w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(data)
    writeFile.close()

urls = (
    'https://onlinetrepreneur.com'
)

data = scrapeURL(urls)
writeCSV(data)