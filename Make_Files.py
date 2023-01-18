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

for i in data:
    try:
        f = open("Spells/" + i[0] + ".html", "w", encoding='utf-8')
    except:
        continue
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<h2>" + i[0] + "</h2>\n")
    f.write("<h3>Level: " + i[2] + "</h3>\n")
    f.write("<h3>Classes: " + i[1] + "</h3>\n")
    f.write("<h4>School: " + i[3] + "</h4>\n")
    f.write("<h4>Casting Time: " + i[4] + "</h4>\n")
    f.write("<h4>Range: " + i[5] + "</h4>\n")
    f.write("<h4>Duration: " + i[6] + "</h4>\n")
    f.write("<h4>Components: ")
    if i[7] == "1": 
        f.write("V ")
    if i[8] == "1": 
        f.write("S ")
    if i[9] == "1": 
        f.write("M ")    
    if i[10] != "":
        f.write("Material Cost: " + i[10])
    f.write("</h4>\n")
    f.write("<p>" + i[11] + "</p>\n")
    f.write("</html>\n")









