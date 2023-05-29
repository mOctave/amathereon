import num2words

data = []
filenames = []
template = """<!DOCTYPE html>
<html lang="en">
\t<head>
\t\t<meta charset="utf-8">
\t\t<meta name="viewport" content="width=device-width, initial-scale=1">
\t\t<title>Amathereon</title>
\t\t<meta name="description" content="A guide to Amathereon: the world and the game.">
\t\t<meta name="author" content="mOctave">
\t\t<link rel="stylesheet" href="style.css">
\t</head>
\t<body onload="bodyInit()">
\t\t<ul class="navbar"></ul>

\t\t<h1>{0}</h1>

\t\t<div class="series" id="series-weapon"></div>

\t\t<p>{2} The average {1} is worth {3} grains of gold and weighs {4} pounds. It is a {5}-handed {6}.</p>

\t\t<p>Damage Type: {7}</p>
\t\t<p>Hit Chance: {8}%</p>
\t\t<p>Damage: {9} - {10}</p>
\t\t<p>Critical Hit Chance: {11}%</p>
\t\t<p>Parry Chance: {12}%</p>


\t\t<hr class="bottom"/>
\t\t<div class="copyright"></div>
\t\t<p class="fineprint">This page was automatically generated. A manually created page would be an appreciated addition.</p>
\t\t<script src="main.js"></script>
\t</body>
</html>
"""

# Line Parsing

def strip(str):
    quotecount = 0
    secondhalf = False
    astring = ""
    bstring = ""
    for char in str:
        if char == '"':
            quotecount += 1
        elif char == ":":
            secondhalf = True
        elif quotecount == 1 and not secondhalf:
            astring += char
        elif secondhalf:
            if quotecount % 2 == 0 and char in  (","," ","\n"):
                pass
            else:
                bstring += char
    return astring, bstring

def parse(a: str, b: str):
    if a == "prototype_parent":
        for entry in data:
            if entry["prototype_key"] == b:
                for prop in entry:
                    if prop != "prototype_key":
                        data[-1][prop] = entry[prop]
    elif not a in ("typeclass","tname"):
        data[-1][a] = b

# Create an html file with the necessary information
def createFiles():
    for i in data:
        filename = i["prototype_key"].lower()
        filenames.append([filename + ".html", i["key"].title()])
        file = open("output/%s.html" % filename,"w")
        rangeText = ""
        if i["range"] == "0":
            rangeText = "melee weapon"
        else:
            if "ammo" in list(i.keys()):
                rangeText = "ranged weapon that takes" + i["ammo"] + "as ammunition"
            else:
                rangeText = "ranged throwing weapon"
        file.write(template.format(i["key"].title(),
                                 i["key"],
                                 i["desc"],
                                 i["value"].strip("Gold()"),
                                 i["mass"],
                                 num2words.num2words(i["hands"]),
                                 rangeText,
                                 i["damageType"].title(),
                                 i["hitChance"],
                                 i["minDamage"],
                                 i["maxDamage"],
                                 i["critChance"],
                                 i["parryChance"],
                                 )
                   )

# Open the file
file = open("data.txt")
protOpen = False

for line in file:
    if not line[0] == "#" and len(line) > 1:
        if protOpen:
            if line[-2] == "}":
                protOpen = False
            else:
                a, b = strip(line)
                parse(a,b)
        if protOpen == False and line[-2] == "{":
            protOpen = True
            data.append({})

file.close()
#print(data)
createFiles()
for i in filenames:
    print('<a href="%s">%s</a><br/>' % (i[0], i[1]))
