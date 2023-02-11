# add(), update(), union(), copy()
friuts = {'apple', 'banana', 'cherry'}
others = {'mango', 'berry', 'water melon'}
# friuts.add('mango')
# print(friuts)
# friuts.update(others)
# print(friuts)
new_set = friuts.union(others)
new_set2 = new_set.copy()
print(new_set2)

# add() - add element to the set
# update() - update the set with the union of this set and others