#Push completed items into lists here, and use them to create stuff.
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

import os
from info import getFranchiseInfo

raritiesFranchises = {
    "High": 20,
    "Medium": 10,
    "Low": 5,
    "Very Low": 1
}

def franchises():
    completedFranchises = []

    for letter in alphabet:
        basepath = 'Franchises/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                franchiseInfo = franchiseFile.read().split("\n")
                if len(franchiseInfo) == 19:
                    completedFranchises.append(entry[0:len(entry)-4:])
    
    completedFranchises.sort()
    masterListFile = open("Master Lists\\Franchises\\franchises.txt", "w", encoding="utf8")
    masterString = ""
    for franchise in completedFranchises:
        masterString = masterString + franchise + "\n"
    masterString = masterString[0:len(masterString)-1:]
    masterListFile.write(masterString)

    masterListFile.close()

    genList = []
    for franchise in completedFranchises:
        franchiseRarity = getFranchiseInfo(franchise, ["popularity"])[0]
        for x in range(raritiesFranchises[franchiseRarity]):
            genList.append(franchise)
    
    genFile = open("Master Lists\\Franchises\\genList.txt", "w", encoding="utf8")
    for gen in genList:
        genFile.write(gen + "\n")
    
    genFile.close()
#prints every completed franchise into franchises.txt. As well, writes the genList based upon the rarities

franchises()