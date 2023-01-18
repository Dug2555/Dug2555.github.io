import os
    
files = os.listdir("./Spells")

f = open("SpellList.html", "w")
f.write("<!DOCTYPE html>\n")
f.write("<html>\n")
f.write("<h1>List of all Spells</h1>\n")
f.write("<body>\n")
f.write("<style>\n body{\n background-image: url('BG2.png');\n}\n</style>\n")
for i in files:
    name = i.replace('.html', '')
    f.write("<p><a href=\"/Spells/" + i + "\">" + name + "</a></p>\n")