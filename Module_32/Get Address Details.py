import re
text = "John Doe, 123 Main St, Anytown USA, 12345"
pattern = '([A-Za-z ]+), ([0-9A-Za-z ]+), ([A-Za-z ]+), ([0-9]+)'
match = re.search(pattern, text)
if match:
    name = match.group(1)
    address = match.group(2)
    city = match.group(3)
    zipcode = match.group(4)

print('Name', name, sep=' : ')
print('Address', address, sep=' : ')
print('City', city, sep=' : ')
print('Zip Code', zipcode, sep=' : ')
