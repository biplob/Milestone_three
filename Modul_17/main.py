# file = open('demo.txt', 'a')
#
# file.writelines('This first demo file for learning'+'\n')
#
# file.close()


with open('demo.txt', 'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
    file.close()











