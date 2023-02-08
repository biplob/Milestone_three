import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.gsmarena.com.bd/upcoming/'
res = requests.get(url)
soup = bs(res.text, 'html.parser')
product_thumbs = soup.findAll('div', {'class': 'product-thumb'})
# print(product_thumbs)
for products in product_thumbs:
    with open('pagelink.csv', 'a+') as file:
        file.writelines(products.find('a').get('href')+'\n')