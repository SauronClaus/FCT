alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
raritiesReverse = {3: "High", 2: "Medium", 1: "Low", 0: "Very Low"}
rarities = {"High": 3, "Medium": 2, "Low": 1, "Very Low": 0}

import os

peopleToFranchise = {}

for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 30:
                    print("Found " + str(characterInfo[0]))
                    try:
                        peopleToFranchise[str(characterInfo[1])].append(entry)
                    except:
                        peopleToFranchise[str(characterInfo[1])] = [entry]

print("That's everyone!")
for franchise in peopleToFranchise.keys():
    highLow = input(franchise + ": ")
    if highLow == "Raise" or highLow == "High" or highLow == "Higher":
        for character in peopleToFranchise[franchise]:
            try:   
                characterFile = open(basepath + "/" + character, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                characterFile.close()
                firstLetter = character[0:1:]
                characterFile = open("Characters\\" + firstLetter + "\\" + character, "w", encoding='utf8')
                    
                newAssembly = characterInfo[0]
                for characterInfoTag in range(1,17):
                    newAssembly = newAssembly + "\n" + characterInfo[characterInfoTag]
                
                currentRarity = characterInfo[17]
                currentRarityNum = rarities[currentRarity]
                if currentRarityNum != 3:
                    newRarityNum = currentRarityNum + 1
                newRarity = raritiesReverse[newRarityNum]
                deuxAssembly = ""
                for characterInfoTag in range(18,30):
                    deuxAssembly = deuxAssembly + "\n" + characterInfo[characterInfoTag]
                characterFile.write(newAssembly + "\n" + newRarity + deuxAssembly)
                characterFile.close()
            except:
                print("Error! " + str(character) + " is not appearing!")
            

                                        