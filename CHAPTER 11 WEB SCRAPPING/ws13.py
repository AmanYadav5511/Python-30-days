import requests
from bs4 import BeautifulSoup

def get_all_paragraphs(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    paragraphs = soup.select('p')
    for paragraph in paragraphs:
      print(paragraph.getText())

get_all_paragraphs('https://www.aaalexports.com')