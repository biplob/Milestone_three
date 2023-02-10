import requests
from bs4 import BeautifulSoup as bs


result_data = {

'sr': '1',
'et': '2',
'exam': 'hsc',
'year': '2022',
'board': 'comilla',
'roll': '552297',
'reg': '1711503740',
'button2': 'Submit'

}
links = 'http://www.educationboardresults.gov.bd/'
result_link = 'http://www.educationboardresults.gov.bd/result.php'

def get_value_s(s, link):
    res = s.get(links)
    soup = bs(res.text, 'html.parser')
    table = soup.find('table', {'class': 'black12bold'})
    trs = table.findAll('tr')
    tds = trs[5].findAll('td')
    captcha_text = tds[1].text
    x, y = captcha_text.split('+')
    value_s = str(int(x)+int(y))
    return value_s


s = requests.Session()
s.headers['headers'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36'
result_data['value_s'] = get_value_s(s, links)
res = s.post(result_link, data=result_data)
soup = bs(res.text, 'html.parser')
tables = soup.findAll('table')
trs = tables[7].findAll('tr')
tds = trs[3].findAll('td')
data_list = []
for td in tds:
    data_list.append(td.text)

print(data_list)

