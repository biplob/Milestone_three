import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = 'https://www.gsmarena.com.bd/xiaomi-redmi-note-12/'
api_data = {} # we use dictinary for json data
res = requests.get(url)
# print(res.text)
data = res.text
soup = bs(data, 'html.parser')
phone_name = soup.find('h1')
# print(heading_tag.text)
api_data['phone_name'] = phone_name.text # for json format
# print(api_data)
phone_div = soup.find('div', {'class': 'col-xs-12 col-sm-6'})
# print(phone_div)
phone_image = soup.find('img').get('src')
api_data['phone_image'] = phone_image # This is for json formate

tables = soup.findAll('table', {'class': 'table_specs'})

for table in tables:
    table_row = table.findAll('tr')
    for row in table_row:
        table_data = row.findAll('td')
        if len(table_data) == 2:
            api_data[table_data[0].text] = table_data[1].text

pprint(api_data)
