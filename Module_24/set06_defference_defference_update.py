x = {'apple', 'banana', 'cherry'}
y = {'google', 'microsoft', 'apple'}

z = x.difference(y)
x.difference_update(y)
print(z)
print(x)