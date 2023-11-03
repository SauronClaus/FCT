numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

infoToIndexFranchises = {
    "name": 0,
    "description": 1,
    "image": 2,
    "article": 3,
    "goals": 4,
    "reach goals": 5,
    "stretch goals": 6,
    "character inserts": 7,
    "antag inserts": 8,
    "minion inserts": 9,
    "artifacts": 10,
    "theme": 11,
    "franchise set": 12,
    "brand": 13,
    "medium": 14,
    "color": 15,
    "popularity": 16,
    "power level": 17,
    "contributors": 18
}

import random

def getFranchiseInfo(franchise, parameters = []):
    firstLetter = franchise[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    
    franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding="utf8")
    franchiseInfo = franchiseFile.read().split("\n")
    returnInfo = []
    for parameter in parameters:
        returnInfo.append(franchiseInfo[infoToIndexFranchises[parameter]])
    return returnInfo

# answers = getFranchiseInfo("Gravity Falls", ["name", "medium", "popularity"])
# print(str(answers[0]) + ": " + str(answers[1]) + ", " + str(answers[2]))
