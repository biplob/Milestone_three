import requests
from bs4 import BeautifulSoup as bs
import csv

with open('test_running.txt', 'r') as file:
    urlist = file.readlines()

# url = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
for url in urlist:
    url = url.strip('\n')
    s = requests.Session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')
    book_name = soup.find('h1').text
    book_price = soup.find('p', {'class': 'price_color'}).text
    image_section = soup.find('div', {'class': 'item active'}).find('img').get('src')
    # product_description = soup.find('div', {'class':'content_inner'}).find('p')
    # product_descriptions = soup.find('p')
    # print(product_description.text)
    book_data = {'book_name': book_name, 'book_price': book_price, 'imag':image_section}
    with open('book_list.csv', 'a', newline='', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=book_data.keys())
        writer.writerow(book_data)