import os
import re

# Get all files from directory of python script

files = os.listdir(os.path.dirname(os.path.abspath(__file__)))

print(files)

# Remove blacklisted files

blacklist = ["index.html","template.html"]

for filename in blacklist:
    files.remove(filename)

print(files)

# Sort files

files = sorted(files)

# Get all remaining html files from the directory

html_files = []

for filename in files:
    result = re.search(".html$", filename)
    if result:
        html_files.append(filename)

print(html_files)

# Get all headings in remaining files

headings = []

for filename in html_files:
    if not filename in blacklist:
        openFile = open(filename, "r")
        firsth1 = re.search("<h1>.*</h1>", openFile.read())
        try:
            headings.append(firsth1.group()[4:-5])
        except:
            pass
        openFile.close()

print(headings)


# Print every entry in the appropriate format

print("")

for i in range(len(headings)):
    print("<li><a href=" + html_files[i] + ">" + headings[i] + "</a></li>")
