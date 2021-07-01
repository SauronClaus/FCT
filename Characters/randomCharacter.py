alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

allCharacters = []
allFranchises = []
import os
import random

exitPath = ""
while exitPath != "End":
    exitPath = input("< >")
    coinFlip = random.randint(1,2)
    # List all files in a directory using os.listdir
    if coinFlip == 1:
        for letter in alphabet:
            basepath = 'Characters/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    characterInfo = characterFile.read()
                    if len(characterInfo.split("\n")) <= 3:
                        allCharacters.append(entry[0:len(entry)-4:])
                    else:
                        print(entry[0:len(entry)-4:])
                    characterFile.close()
        
        
        
        print("Choosing from " + str(len(allCharacters)) + " characters.")
        ranNum = random.randint(0,len(allCharacters)-1)
        characterFile = open("Characters\\" + allCharacters[ranNum][0:1:] + "\\" + allCharacters[ranNum] + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")
        print(characterInfo[0] + " (" + characterInfo[1] + ")!")
    else:
        for letter in alphabet:
            basepath = 'Franchises/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read()
                    if len(franchiseInfo.split("\n")) <= 1:
                        allFranchises.append(entry[0:len(entry)-4:])
                    else:
                        print(entry[0:len(entry)-4:])
        print("Choosing from " + str(len(allFranchises)) + " franchises.")
        ranNum = random.randint(0,len(allFranchises)-1)
        print(allFranchises[ranNum] + "!")