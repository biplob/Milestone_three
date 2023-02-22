import re
url = "http://www.example.com/path/to/page"
pattern = "(?:https?://)?(?:www\.)?([A-Za-z0-9-]+\.[A-Za-z]{2,})" # if we need to collect full url then use the line /([A-Za-z]+/([a-zA-Z])+/[a-zA-Z]+)
match = re.search(pattern, url)
if match:
    domain = match.group(1)
    print('Domain',domain, sep=' : ')