alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
franchisesFull = {}
import os

exitPath = ""
while exitPath != "End":
    exitPath = input("Enter the old franchise: ")
    if exitPath != "End":
        charactersReplace = []
        newFranchise = input("Enter the franchise to replace it with: ")
        # List all files in a directory using os.listdir
        for letter in alphabet:
            basepath = 'Characters/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    characterInfo = characterFile.read()
                    if len(characterInfo.split("\n")) >= 3:
                        characterInformation = characterInfo.split("\n")
                        oldFranchise = characterInformation[1]
                        characterName = characterInformation[0]
                        if oldFranchise == exitPath:
                            if len(characterInfo.split("\n")) >= 17:
                                charactersReplace.append(characterName)
                            else:
                                charactersReplace.append(characterName + " (!)")
                            characterInformation.remove(characterName)
                            characterInformation.remove(characterInformation[0])

                            characterFile.close()

                            characterFile = open(basepath + "/" + entry, "w", encoding='utf8')
                            characterFile.write(characterName + "\n")
                            characterFile.write(newFranchise)
                            for extraInfo in characterInformation:
                                characterFile.write("\n" + extraInfo)
                            characterFile.close()

        characterString = ""        
        for character in charactersReplace:
            characterString = characterString + character + ", "
        characterString = characterString[0:len(characterString)-2:]
        print("Replaced for " + characterString)
