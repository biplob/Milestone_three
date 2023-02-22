import re
text = "Please contact us at support@eample.com for more information. Also you can help@support.com"
pattern = '[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+'
# email = re.search(pattern, text)
# print(email.group())
email = re.findall(pattern, text)
print(email)

