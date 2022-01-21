# Reads the tags in tags.txt, and redoes the people tags with them.
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
from colors import colors
import os

completedCharacters = []
undoneCharacters = []
needToUpdateCharacters = []
weirdCharacters = []
allCharacters = []
print("Start!")
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 30:
                completedCharacters.append(entry[0:len(entry)-4:])
            else:
                if len(characterInfo) == 5:
                    undoneCharacters.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 17 or len(characterInfo) == 22 or len(characterInfo) == 24 or len(characterInfo) == 29:
                        needToUpdateCharacters.append(entry[0:len(entry)-4:])
                    else:
                        weirdCharacters.append(entry[0:len(entry)-4:])
            allCharacters.append(entry[0:len(entry)-4:])
            #if characterInfo[0] != entry[0:len(entry)-4:]:
                #print("Check " + characterInfo[0] + " (" + entry[0:len(entry)-4:] + ")")

for character in completedCharacters:
    firstLetter = character[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    tagsExpended = []
    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
    characterInfo = characterFile.read().split("\n")
    characterFile.close()
    if characterInfo[28] == "":
        print(character + " has errors.")
        newAssembly = characterInfo[0]
        for characterInfoTag in range(1,23):
            newAssembly = newAssembly + "\n" + characterInfo[characterInfoTag]
        #newAssembly = newAssembly + "\n" + "COLOR"
        #print("[\n" + newAssembly + "\n]")
        deuxAssembly = ""
        for characterInfoTag in range(24,28):
            deuxAssembly = deuxAssembly + "\n" + characterInfo[characterInfoTag]
        print("<\n" + newAssembly + "\nCOLOR" + deuxAssembly + "\n>")
        print("-" + characterInfo[23] + "-")
        powers = ""
        colorChoice = ""
        for color in colors.keys():
            if color in characterInfo[23]:
                print("Found " + color + " in " + characterInfo[23])
                colorChoice = color
                powers = characterInfo[23][len(color):len(characterInfo[23]):]
        print("[" + colorChoice + "\n" + powers + "]")
        print("{" + newAssembly + "\n" + colorChoice + "\n" + powers + deuxAssembly + "\n}")

        characterW = open("Characters\\" + firstLetter + "\\" + character + ".txt", "w", encoding='utf8')
        characterW.write(newAssembly + "\n" + colorChoice + "\n" + powers + deuxAssembly)
        print("done")
        characterW.close()



