# This program fills out all of the files under Statistics\\Characters

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

chooseFranchise = input("Enter franchise (the second level): ")
chooseBrand = input("Enter brand: ")


# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 29:
                if characterInfo[21] == chooseFranchise:
                    firstLetter = entry[0:1:]
                    if firstLetter in numbers:
                        firstLetter = "#"
                    characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "w", encoding='utf8')
                    print("Found " + characterInfo[0])
                    newAssembly = characterInfo[0]
                    for characterInfoTag in range(1,25):
                        newAssembly = newAssembly + "\n" + characterInfo[characterInfoTag]
                    #newAssembly = newAssembly + "\n" + "COLOR"
                    #print("[\n" + newAssembly + "\n]")
                    brand = chooseBrand
                    deuxAssembly = ""
                    for characterInfoTag in range(26,29):
                        deuxAssembly = deuxAssembly + "\n" + characterInfo[characterInfoTag]
                    
                    characterFile.write(newAssembly + "\n" + brand + deuxAssembly)