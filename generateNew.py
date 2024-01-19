numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

rarities = {
    "High": 20,
    "Medium": 10,
    "Low": 5,
    "Very Low": 1
}

import random
from info import getFranchiseInfo

def generateFranchise(restrictions = "None", franchise = "None"):
    if franchise == "None":
        genList = open("Master Lists\\Franchises\\genList.txt", "r", encoding="utf8").read().split("\n")
        RNG = random.randint(0, len(genList))
        chosenFranchise = genList[RNG]

        print("Generated [" + chosenFranchise + "]")
    else:
        print("Override: Franchise is [" + franchise + "]")
        chosenFranchise = franchise
    return(chosenFranchise)
#Generates a franchise to use.

def generateMatch(restrictions = "None", franchise = "None", featuredCharacters = []):
    print("Oh no.")