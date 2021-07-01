#alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet = ["A"]
tagsFull = {}
import os

exitPath = ""
while exitPath != "End":
    exitPath = input("Enter the old tag: ")
    if exitPath != "End":
        charactersReplace = []
        newTag = input("Enter the tag to replace it with: ")
        # List all files in a directory using os.listdir
        for letter in alphabet:
            basepath = 'Characters/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    characterInfo = characterFile.read()
                    if len(characterInfo.split("\n")) >= 16:
                        characterInformation = characterInfo.split("\n")
                        tagList = characterInformation[13].split(",")
                        characterName = characterInformation[0]
                        characterRarity = characterInformation[15]
                        characterPowerLevel = characterInformation[14]
                        #print(characterName + " (" + str(tagList[0]) + ")")
                        if exitPath in tagList:

                            tagList.remove(exitPath)

                            tagListString = ""
                            for tag in tagList:
                                tagListString = tagListString + tag + ","
                            tagListString = tagListString + newTag
                            charactersReplace.append(characterName)

                            characterInformation.remove(characterRarity)
                            characterInformation.remove(characterPowerLevel)
                            characterInformation.remove(characterInformation[13])

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
