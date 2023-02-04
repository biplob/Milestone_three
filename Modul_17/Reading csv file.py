import csv

# with open('demo.txt', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

new_blank = []
with open('student.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        new_blank.append(row)

print(new_blank)