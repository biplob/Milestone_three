import re
text = "Please contact us at Support@example.com for more information"
pattern = r'[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z0-9]+'
# match = re.search(pattern, text)
# print(match)
new_text = re.sub(pattern, lambda x:x.group().lower(), text)
print(new_text)