from bs4 import BeautifulSoup
import requests

source = requests.get('http://anatolia.com').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
#print(article.prettify())

headline = article.h2.a.text
print(headline)