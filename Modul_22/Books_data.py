import requests
from bs4 import BeautifulSoup as bs
import csv

with open('alllinks.txt', 'r') as file:
    urllist = file.readlines()
# print(urllist)

# url = 'https://books.toscrape.com/catalogue/the-bear-and-the-piano_967/index.html'

for url in urllist:
    url = url.strip('\n')
    s = requests.Session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')
    book_name = soup.find('h1').text
    book_price = soup.find('p', {'class': 'price_color'}).text
    image_section = soup.find('div', {'class': 'item active'}).find('img').get('src')
    book_data = {'book_name': book_name, 'book_price': book_price, 'img': image_section}
    with open('book_data.csv', 'a', newline='', encoding='utf8') as file:
        writer = csv.DictWriter(file, fieldnames=book_data.keys())
        writer.writerow(book_data)

