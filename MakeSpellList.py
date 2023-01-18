import os
    
files = os.listdir("./Spells")

f = open("SpellList.html", "w")
f.write("<!DOCTYPE html>\n")
f.write("<html>\n")
f.write("<h1>List of all Spells</h1>\n")
f.write("<body>\n")
for i in files:
    name = i.replace('.html', '')
    f.write("<p><a href=\"/Spells/" + i + ".html\">" + name + "</a></p>\n")