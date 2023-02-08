import requests
from bs4 import BeautifulSoup as bs

i = 1
while i <= 50:
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    r = requests.Session()
    res = r.get(url)
    soup = bs(res.text, 'html.parser')
    main_div = soup.find('div', {'class': 'col-sm-8 col-md-9'})
    # links = main_div.findAll('a')
    # all_links = []
    # for link in links:
    #     all_links.append('https://books.toscrape.com/'+link.get('href'))
    #
    # single_name = main_div.find('h3')
    # print(single_name.find('a'))
    headings = main_div.findAll('h3')

    for heading in headings:
        link = 'https://books.toscrape.com/'+heading.find('a').get('href')
        with open('test_running.txt', 'a') as file:
            file.writelines(link+'\n')
    i += 1