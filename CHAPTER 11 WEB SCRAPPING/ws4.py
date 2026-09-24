from bs4 import BeautifulSoup
import requests

source = requests.get('http://poper.ai.').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
#print(article.prettify())

#headline = article.a.text
#print(headline)

#summary = article.find('div', class_='entry-media')
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')
print(vid_src)