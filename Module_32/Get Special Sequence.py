import re
s = 'He is 65 years old!'
s_2 = 'Bangaldesh ogt Independence day in 16th December 1971'
match = re.search('[0-9][0-9]', s)
match_2 = re.search('\d+', s)
match_3 = re.findall('\d+', s_2)
# print('Print of X is',match)
# print('Print of X.span() is',match.span())
# print('Print of X.Groups() is',match.groups())
# print('Print of X.staring is',match.string)
# print(match_2)
# print(match_2.group())
print(match_3)


