import csv

lodata = {}
MySpells = []
SpellsToAdd = {}
with open("dnd-spells.csv", 'r', encoding='utf-8') as spells:
    data = csv.DictReader(spells)
    lodata = list(data)

with open("MySpellList.txt", 'r') as mine:
    MySpells = mine.read().splitlines()

print(MySpells)
for i in lodata:
    if i["name"] in MySpells:
        if i["level"] not in SpellsToAdd:
            SpellsToAdd[i["level"]] = [i["name"]]
        else:
            SpellsToAdd[i["level"]].append(i["name"])

print(SpellsToAdd)



f = open("Amond.html", "w")
f.write("<h1>Amond Maslo Karridi</h1>\n<h1></h1>\n<h2>Spells:</h2>\n")

f.write("<h3>Cantrips:</h3>\n")
try:
    for i in SpellsToAdd["0"]:
        f.write("<p><a href=\"/Spells/" + i + ".html\">" + i + "</a></p>\n")
except:
    pass

f.write("<h3>Level 1:</h3>\n")
for val in range(0,4):
    f.write("<input type = \"checkbox\">\n")
try:
    for i in SpellsToAdd["1"]:
        f.write("<p><a href=\"/Spells/" + i + ".html\">" + i + "</a></p>\n")
except:
    pass

f.write("<h3>Level 2:</h3>\n")
for val in range(0,3):
    f.write("<input type = \"checkbox\">\n")
try:
    for i in SpellsToAdd["2"]:
        f.write("<p><a href=\"/Spells/" + i + ".html\">" + i + "</a></p>\n")
except:
    pass

f.write("<h3>Level 3:</h3>\n")
for val in range(0,2):
    f.write("<input type = \"checkbox\">\n")
try:
    for i in SpellsToAdd["3"]:
        f.write("<p><a href=\"/Spells/" + i + ".html\">" + i + "</a></p>\n")
except:
    pass

f.write("<h3>Level 4:</h3>\n")
for val in range(0,2):
    f.write("<input type = \"checkbox\">\n")
try:
    for i in SpellsToAdd["4"]:
        f.write("<p><a href=\"/Spells/" + i + ".html\">" + i + "</a></p>\n")
except:
    pass