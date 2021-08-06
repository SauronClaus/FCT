alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

tagFile = open("tags.txt", "r", encoding='utf8')
tagsList = tagFile.read().split("\n")
characters = {}


for tagSet in tagsList:
    tagSetList = tagSet.split("; ")
    tag = tagSetList[0]
    peopleAttachedFull = tagSetList[1]
    peopleAttached = peopleAttachedFull.split(", ")
    for character in peopleAttached:
        #print(character)
        if len(character.split("|")) == 1:
            tagsExpended = []
            
            try:
                characters[character].append(tag)
            except:
                characters[character] = []
                characters[character].append(tag)
        else:
            #print("-" + character)
            charactersNames = character.split("|")
            characterName = charactersNames[0]
            pairedName = charactersNames[1]
            firstLetter = characterName[0:1:]
            if firstLetter in numbers:
                firstLetter = "#"
            tagsExpended = []
            characterFile = open("Characters\\" + firstLetter + "\\" + characterName + ".txt", "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")

            try:
                characters[characterName].append(tag + "|" + pairedName)
            except:
                characters[characterName] = []
                characters[characterName].append(tag + "|" + pairedName)

characterSearch = "Iron Man"
stringInfo = ""
for tag in characters[characterSearch]:
    stringInfo = stringInfo + tag + ", "
print(characterSearch + ": " + stringInfo[0:len(stringInfo)-2:])

for character in characters.keys():
    firstLetter = character[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
    characterInfo = characterFile.read().split("\n")
    
    characterFile.close()
    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "w", encoding='utf8')
    
    tagString = ""
    for tag in characters[character]:
        tagString = tagString + tag + ","
    print(tagString[0:len(tagString)-1:])

    for item in characterInfo:
        if characterInfo.index(item) != 15 and characterInfo.index(item) != 23:
            characterFile.write(item + "\n")
        else:
            if characterInfo.index(item) == 23:
                characterFile.write(item)
            else:
                if characterInfo.index(item) == 15:
                    characterFile.write(tagString[0:len(tagString)-1:] + "\n")
    characterFile.close()

print("Completed!")