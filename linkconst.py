# Code is a mildly adapted version of this SO answer. https://stackoverflow.com/a/56381857

import glob

# Point mypath to the highest folder you want all the assets for e.g. "C:\Users\Baliff\Documents\GitHub\Meekins.github.io".
# Your username is what appears in the "Username.github.io" link
mypath=r"INSERT_FILEPATH_HERE"
githubUsername="ExampleUser"

# Change r'\**\*.gif' to whatever extension you want to generate links for.
files = glob.glob(mypath + r'\**\*.gif', recursive=True)

# print(files) # as list
for f in files:
    splitResult = f.split(".github.io")
    splitResult = "https://" + githubUsername + ".github.io" + splitResult[1]
    print(splitResult) # nice looking single line per file
