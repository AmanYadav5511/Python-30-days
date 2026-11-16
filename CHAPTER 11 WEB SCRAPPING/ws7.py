import requests
res = requests.get('https://www.aaalexports.com')
print(res.raise_for_status)
print(res.text[:250])