import requests
from bs4 import BeautifulSoup as bs

i = 1
while i <= 50:
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'
    s = requests.session()
    res = s.get(url)
    soup = bs(res.text, 'html.parser')
    data_div = soup.find('div', {'class': 'col-sm-8 col-md-9'})
    # links = data_div.findAll('a')
    # all_links = []
    # for link in links:
    #     all_links.append('https://books.toscrape.com/'+link.get('href'))
    #
    # all_links.pop()
    # print(all_links)

    # single_name = data_div.find('h3')
    # print(single_name.find('a'))
    headings = data_div.findAll('h3')
    for heading in headings:
        link = 'https://books.toscrape.com/'+heading.find('a').get('href')
        with open('alllinks.txt', 'a') as file:
            file.writelines(link+'\n')
    i += 1