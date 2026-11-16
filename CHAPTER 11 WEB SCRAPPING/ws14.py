import requests
from bs4 import BeautifulSoup

def list_link_urls(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('a')
    for linkTag in links:
      href = linkTag.get('href')

      if href:
         print(href)

list_link_urls('https://www.aaalexports.com')