import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
playFile = open('romeoandjuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()