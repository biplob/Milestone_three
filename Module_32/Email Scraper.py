import re
s = 'I am monsur. my email address is monsur25@gmail.com. I can extract this'
x = re.findall(r'[\w+]+@+[\w+]+\.\w+',s)
# print(x)
print(x.group())
