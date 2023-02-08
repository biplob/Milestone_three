import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.gsmarena.com.bd/motorola-moto-g23/'
api_data = {} # for json format
res = requests.get(url)
data = res.text
# print(res.text)
soup = bs(data, 'html.parser')
phone_name = soup.find('h1')
api_data['phone_name'] = phone_name.text # for api formate
phone_div = soup.find('div', {'class': 'col-xs-12 col-sm-6'})
# print(phone_div)
phone_image = phone_div.find('img').get('src')
# print(phone_image)
api_data['phone_image'] = phone_image
# print(api_data)
tables = soup.findAll('table', {'class': 'table_specs'})
# print(tables)
for table in tables:
    table_row = table.findAll('tr')
    for row in table_row:
        table_data = row.findAll('td')
        if len(table_data) == 2:
            api_data[table_data[0].text] = table_data[1].text


pprint(api_data)
