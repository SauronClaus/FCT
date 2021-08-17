import os
adjectives = []
deleteAdjectives = []

for x in range(1,5):
    readFile = open("Adjectives\\Tier " + str(x) + ".txt", "r", encoding='utf8')
    readInfo = readFile.read().split("\n")
    for adjective in readInfo:
        if adjective[len(adjective)-1::] != "-":
            adjectives.append(adjective[0:len(adjective)-1:])
        else:
            adjectives.append(adjective)
basepath = "Adjectives\\Descriptions"
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        adjectiveFileName = entry[0:len(entry)-4:]
        if not(adjectiveFileName in adjectives):
            deleteAdjectives.append(adjectiveFileName)
        else:
            adjectives.remove(adjectiveFileName)

for adjective in deleteAdjectives:
    print("Delete: " + adjective)
for adjective in adjectives:
    print("Add: <" + adjective + ">")