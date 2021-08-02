alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


import os

groupsLarge = {}

writeFile = open("addBeforeItBreaks.txt","w",encoding='utf8')
write2File = open("franchiseCharacters.txt","w",encoding='utf8')

charactersToFind = []
print("Start!")

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Franchises/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
            franchiseInfo = franchiseFile.read().split("\n")
            if len(franchiseInfo) == 5:
                characters = franchiseInfo[4].split("|")
                characterString = ""
                for character in characters:
                    charactersToFind.append(character)
                    characterString = characterString + character + ", "
                write2File.write(franchiseInfo[0] + ": " + characterString[0:len(characterString)-2:] + "\n")

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                if entry[0:len(entry)-4:] in charactersToFind:
                    while entry[0:len(entry)-4:] in charactersToFind:
                        print(entry[0:len(entry)-4:])
                        charactersToFind.remove(entry[0:len(entry)-4:])   

singular = []
charactersToFind.sort()

for character in charactersToFind:
    if not(character in singular):
        singular.append(character)

for character in singular:
    writeFile.write(character + "\n")

print("Completed!")