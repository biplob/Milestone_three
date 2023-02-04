file = open('demo.txt', 'r')
data = file.readlines()
file.close()

new_data = []
for element in data:
    new = element.strip('\n')
    new_data.append(new)


print(new_data)
