import requests
res = requests.get('https://google.com/nothinghere123')
try:
    res.raise_for_status()
except Exception as exc:
      print('There was a problem: %s' % (exc))