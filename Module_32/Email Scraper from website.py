from requests import get
import re

url = 'https://www.infohindihub.in/2021/03/free-bulk-email-id-list-1000-active.html'

res = get(url)
x = re.findall('[\w]+@[\w]+\.[\w]+', res.text)
with open('emails.csv', 'a+') as file:
    file.writelines(x)

