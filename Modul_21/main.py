from requests import get
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.com/essence-Princess-Effect-Mascara-Cruelty/dp/B00T0C9XRK/ref=lp_23824701011_1_2'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Cookie'  :'session-id=133-1078166-4081106; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=130-1548306-2335153; lc-main=en_US; skin=noskin; __utmc=194891197; __utmz=194891197.1675668505.20.12.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not provided); __utma=194891197.1242212445.1673529868.1675679453.1675688316.22; session-token="5JSBQR7ppIWeyNTZyob6mcnBkGhEwXpLf2ZX2fxSkoA/t46izdRaOY066frTLOPfyBeO4tv6tc3RrUprFp+Et+sNr9HSCLJnlGAppVpPzXi5eg9KS/mNFJRe9sa7co8drqxqglt/B7Qtj1mUYAwm/snpGe6HlFVnVyImOXpBFuwzfJG6JSAhjVyTdVQP7g7EiVi97JnccpziHQDGI0l/F6lfoO8EGuqKo6eoixbz+1E="; __utmb=194891197.6.10.1675688316'
}

res = get(url, headers=header)
soup = bs(res.text, 'html.parser')
product_title = soup.find('span', {'id': 'productTitle'})
product_details_table = soup.find('table', {'class': 'a-normal a-spacing-micro'})
product_details_row = soup.findAll('tr')

product_space = {}
for product_row in product_details_row:
    product_data = product_row.findAll('td')
    if len(product_data) > 1:
        product_space[product_data[0].text.strip()] = product_data[1].text.strip()

product_space['title'] = product_title.text
print(product_space)


