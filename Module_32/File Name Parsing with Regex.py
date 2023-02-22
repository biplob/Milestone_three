import re
filename = "image_2021-03-12_12-34-56.jpg"
pattern = "^(.*)_(\d{4}-\d{2}-\d{2})_(\d{2}-\d{2}-\d{2})\.(.*)$"
match = re.search(pattern, filename)
if match:
    prefix = match.group(1)
    date = match.group(2)
    time = match.group(3)
    extension = match.group(4)
    print('Prefix', prefix, sep= '-----')
    print('Date', date, sep='-----')
    print('Time', time, sep='-----')
    print('Extension', extension, sep='-----')