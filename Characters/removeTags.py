alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#alphabet = ["#"]
tagsFull = {}
import os

deleteTags = ["Books", "Video Games", "Movies", "TV Shows", "Comic Books", "Superhero Comics", "CGI", "Webcomics", "Webtoons", "Anime", "Graphic Novels", "Manga"]
for exitPath in deleteTags:
    charactersReplace = []
    # List all files in a directory using os.listdir
    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read()
                if len(characterInfo.split("\n")) >= 16:
                    characterInformation = characterInfo.split("\n")
                    tagList = characterInformation[14].split(",")
                    characterName = characterInformation[0]
                    characterRarity = characterInformation[16]
                    characterPowerLevel = characterInformation[15]
                    #print(characterName + " (" + str(tagList[0]) + ")")
                    if exitPath in tagList:

                        tagList.remove(exitPath)

                        tagListString = ""
                        for tag in tagList:
                            tagListString = tagListString + tag + ","
                        tagListString = tagListString[0:len(tagListString)-1:]
                        charactersReplace.append(characterName)

                        characterInformation.remove(characterRarity)
                        characterInformation.remove(characterPowerLevel)
                        characterInformation.remove(characterInformation[14])

                        characterFile.close()

                        characterFile = open(basepath + "/" + entry, "w", encoding='utf8')

                        for extraInfo in characterInformation:
                            characterFile.write(extraInfo + "\n")
                        characterFile.write(tagListString + "\n")
                        characterFile.write(characterPowerLevel + "\n")
                        characterFile.write(characterRarity)
                        characterFile.close()

    characterString = ""        
    for character in charactersReplace:
        characterString = characterString + character + ", "
    characterString = characterString[0:len(characterString)-2:]
    print("Replaced for " + characterString)
