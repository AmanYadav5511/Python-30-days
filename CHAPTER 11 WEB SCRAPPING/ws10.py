from bs4 import BeautifulSoup
html = '<p>Hello <b>World</b></p>'
soup = BeautifulSoup(html, 'html.parser')
print(soup)