import requests
from bs4 import BeautifulSoup as bs

s = requests.session()
url = 'http://quotes.toscrape.com/login'
payload = {
    'username': 'admin',
    'password': 'admin'
}

res = requests.post(url, data= payload)
print(res.text)