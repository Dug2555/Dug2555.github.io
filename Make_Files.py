import csv
data = []
with open("dnd-spells.csv", "r", encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.append(row)

for i in data:
    print(i)