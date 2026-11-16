import requests
res = requests.get('https://www.google.com')
print(res.status_code)

#200 means connection was succesfull