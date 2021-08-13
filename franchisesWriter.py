alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

completedCharacters = []
undoneCharacters = []
needToUpdateCharacters = []
weirdCharacters = []
allCharacters = []
franchiseList = {}

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                completedCharacters.append(entry[0:len(entry)-4:])
            else:
                if len(characterInfo) == 5:
                    undoneCharacters.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 17 or len(characterInfo) == 22:
                        needToUpdateCharacters.append(entry[0:len(entry)-4:])
                    else:
                        weirdCharacters.append(entry[0:len(entry)-4:])
            allCharacters.append(entry[0:len(entry)-4:])
            #if characterInfo[0] != entry[0:len(entry)-4:]:
                #print("Check " + characterInfo[0] + " (" + entry[0:len(entry)-4:] + ")")

for character in allCharacters:
    firstLetter = character[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    
    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
    characterInfo = characterFile.read().split("\n")

    characterFranchise = characterInfo[1]
    
    try:
        franchiseList[characterFranchise].append(character)
    except:
        franchiseList[characterFranchise] = [character]

franchises = []

for franchise in franchiseList:
    franchises.append(franchise)

franchises.sort()
franchiseFile = open("franchisesFinal.txt", "w", encoding='utf8')

for franchise in franchises:
    testString = franchise + ": "
    for character in franchiseList[franchise]:
        testString = testString + character + ", "
    testString = testString[0:len(testString)-2:]
    franchiseFile.write(testString + "\n")