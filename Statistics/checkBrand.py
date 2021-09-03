# This program fills out all of the files under Statistics\\Characters

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os
brandsFile = open("Statistics\\brands.txt", "w",encoding='utf8')
unFile = open("Statistics\\incompletePeople.txt", "w", encoding='utf8')
completedCharacters = []
brandsList = []
brandsDict = {}

unList = []
unDict = {}
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 29:
                if characterInfo[25] != "":
                    try:
                        if not(characterInfo[25] in brandsList):
                            brandsList.append(characterInfo[25])
                        brandsDict[characterInfo[25]].append(entry[0:len(entry)-4:])
                    except:
                        if not(characterInfo[25] in brandsList):
                            brandsList.append(characterInfo[25])
                        brandsDict[characterInfo[25]] = [entry[0:len(entry)-4:]]
                if characterInfo[25] == "":
                    try:
                        if not(characterInfo[21] in unList):
                            unList.append(characterInfo[21])
                        unDict[characterInfo[21]].append(entry[0:len(entry)-4:])
                    except:
                        if not(characterInfo[21] in unList):
                            unList.append(characterInfo[21])
                        unDict[characterInfo[21]] = [entry[0:len(entry)-4:]]


brandsList.sort()
unList.sort()

for brand in brandsList:
    brandString = brand + ": "
    for person in brandsDict[brand]:
        brandString = brandString + person + ", "
    brandString = brandString[0:len(brandString)-2:]
    brandsFile.write(brandString + "\n")

for brand in unList:
    brandString = brand + ": "
    for person in unDict[brand]:
        brandString = brandString + person + ", "
    brandString = brandString[0:len(brandString)-2:]
    unFile.write(brandString + "\n")