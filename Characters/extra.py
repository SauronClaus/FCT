
franchiseCollectionFile = open("Characters\\tiedFranchises.txt", "r", encoding="utf8")
franchiseCollections = franchiseCollectionFile.read().split("\n")
for franchiseTag in franchiseCollections:
    #print("-" + tagTie)
    franchiseList = franchiseTag.split(";")[1]
    franchiseCollectionName = franchiseTag.split(";")[0]
    franchiseNewCollection = {franchiseCollectionName : 0}
    for franchise in franchiseList.split(","):
        newNum = franchisesFull[franchise]
        del franchisesFull[franchise]
        franchiseNewCollection = {franchise : newNum}
        print("Franchise: " + franchise)
        franchiseAllCollections.append(franchiseNewCollection)