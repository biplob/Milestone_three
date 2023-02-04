import csv
student = {'name': 'Monsur Biplob', 'email': 'monsur.biplob93@gmail.com', 'fb_id': 'https:fb.com/monsurbiplob', 'age': '26'}


with open('student.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=student.keys())
    writer.writeheader()
    i = 0
    while i < 1000:
           writer.writerow(student)
           i += 1