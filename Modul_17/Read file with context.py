# with open('demo.txt', 'r') as file:
#     data = file.readline()
#
# print(data)

str_1 = 'This line for cheking'

i = 0
while i < 100:
        with open('text.txt', 'a') as file:
                 file.writelines(str_1+'\n')
        i += 1

