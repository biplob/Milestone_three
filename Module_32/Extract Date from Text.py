import re
text = "His date of birth is 12/31/1975"
pattern = '\d{1,2}/\d{1,2}/\d{4}'
date = re.search(pattern, text)
# print(date)
print(date.group())