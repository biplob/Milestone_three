import re
log = " 2021-03-12 10:15:30 [ERROR] Failed to connect to database\n2021-03-12 11:2345 [WARNING] Low disk space\n2021-03-12 12:34:56 [ERROR] Internal Server error"
pattern = "(\d{4}-\d{2)-\d{2} \d{2}:\d{2}:\d{2}) \[(ERROR|WARNING)\] (.*)"

for match in re.finditer(pattern, log):
    timestamp = match.group(1)
    level = match.group(2)
    message = match.group(3)

    print('TimeStamp', timestamp, sep=' :')
    print('Lavel', level, sep=' :')
    print('Message', message, sep=' :')
