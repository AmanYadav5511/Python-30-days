import requests
from bs4 import BeautifulSoup

def count_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('a')
    print(len(links))

count_links('https://aaalexports.com')