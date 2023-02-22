import re
ba = 'Bangla123desh'
match = re.search('123', ba)
print(match)
ba[6:9]


# s = 'Banagla123desh'
#
# if '123' in s:
#     print("123 Present")
#     print('using find', s.find('123'))
#     print('using index',s.index('123'))
# else:
#     print("123 Unpresent")
# print(s[7:])