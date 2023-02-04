import csv
Games = ['Football', 'Cricket', 'Bolibowal', 'Swiming', 'Running', 'Cycling']

with open('games.csv', 'a', newline='\n') as f:
    writer = csv.writer(f)
    writer.writerow(Games)