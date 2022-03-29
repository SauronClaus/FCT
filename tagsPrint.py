# Prints all the tags in the bot to tags.txt.
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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

tags = {}
for character in completedCharacters:
    firstLetter = character[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    tagsExpended = []
    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
    characterInfo = characterFile.read().split("\n")

    tagSearch = "Water Bender"
    if characterInfo[15] != "":
        characterTagList = characterInfo[15].split(",")
        for characterTagFull in characterTagList:
            pairedTag = False
            if len(characterTagFull.split("|")) > 1:
                pairedTag = True
            characterTag = characterTagFull.split("|")[0]
            if tagSearch == characterTag:
                print("Tag Match: " + characterInfo[0] + " (" + character + ") has the " + characterTag + " (" + tagSearch + ") tag!")
            if not (characterTag in tagsExpended):
                if pairedTag == False:
                    try:
                        tags[characterTag].append(character)
                    except:
                        tags[characterTag] = []
                        tags[characterTag].append(character)
                    #tagsExpended.append(characterTag)
                else:
                    try:
                        tags[characterTag].append(character + "|" + characterTagFull.split("|")[1])
                    except:
                        tags[characterTag] = []
                        tags[characterTag].append(character + "|" + characterTagFull.split("|")[1])
                    #tagsExpended.append(characterTag)
            #else:
                #print(characterInfo[0] + " already expended " + characterTag)

tagsPart2 = []
for tag in tags.keys():
    tagsPart2.append(tag)
tagFile = open("tags.txt", "w",encoding='utf8')
tagsPart2.sort()
for tag in tagsPart2:
    tagString = tag + "; "
    for character in tags[tag]:
        tagString = tagString + character + ", "
    tagString = tagString[0:len(tagString)-2:] + "\n"
    tagFile.write(tagString)
print("Completed!")