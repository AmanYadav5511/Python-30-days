import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.select('title')
    print(title[0].get_text())

get_page_title('https://www.aaalexports.com')