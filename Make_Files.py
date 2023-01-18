import csv
import os

data = []
with open("dnd-spells.csv", "r", encoding='utf-8') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        data.append(row)


print(data[0])

try:
    os.mkdir("./Spells")
except OSError as error: 
    print("Already made")

# for i in data:
    i = data[1]
    f = open("Spells/" + i[0] + ".html", "w")
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<h2>" + i[0] + "</h2>\n")
    f.write("<h3>" + i[2] + " " + i[1] + "</h3>\n")
    f.write("<h4>" + i[3] + " " + i[4] + " " + i[5] + "</h4>\n")
    f.write("<h4>" + i[6] + " ")
    if i[7] == 1: 
        f.write("V ")
    if i[8] == 1: 
        f.write("S ")
    if i[9] == 1: 
        f.write("M ")    
    f.write(i[10] + "</h4>\n")
    f.write("<p>" + i[11] + "</p>\n")
    f.write("</html>\n")









