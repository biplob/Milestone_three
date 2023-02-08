import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com.bd/'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
product_thumbss = soup.findAll('div', {'class': 'product-thumb'})
# print(product_thumbss)
for product in product_thumbss:
    with open('product.csv', 'a+') as file:
        file.writelines(product.find('a').get('href')+'\n')