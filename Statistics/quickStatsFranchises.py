# This program fills out all of the files under Statistics\\Franchises

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

def quickStatsFranchise():
    completedFranchises = []
    undoneFranchises = []
    needToUpdateFranchises = []
    weirdFranchises = []
    allFranchises = []

    for letter in alphabet:
        basepath = 'Franchises/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                franchiseInfo = franchiseFile.read().split("\n")
                if len(franchiseInfo) == 18:
                    completedFranchises.append(entry[0:len(entry)-4:])
                else:
                    if len(franchiseInfo) == 7 or len(franchiseInfo) == 17:
                        needToUpdateFranchises.append(entry[0:len(entry)-4:])
                    else:
                        if len(franchiseInfo) == 2:
                            undoneFranchises.append(entry[0:len(entry)-4:])
                        else:
                            #print(entry[0:len(entry)-4] + ": " + str(len(franchiseInfo)))
                            weirdFranchises.append(entry[0:len(entry)-4:])
                allFranchises.append(entry[0:len(entry)-4:])

    completedFranchises.sort()
    undoneFranchises.sort()
    needToUpdateFranchises.sort()
    weirdFranchises.sort()


    franchiseBrands = {}
    franchiseBrandsFile = open("Statistics\\Franchises\\franchiseBrands.txt", "w",encoding='utf8')

    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")
        searchFranchise = ""

        franchiseBrand = franchiseInfo[12]
        franchiseFranchise = franchiseInfo[11]
        if franchiseFranchise == searchFranchise:
            print("-" + franchiseInfo[0] + " (" + franchise + ") is in " + franchiseBrand + ": " + franchiseFranchise + " (Franchise)")
        try:
            franchiseBrands[franchiseBrand][franchiseFranchise].append(franchise)
            franchiseBrands[franchiseBrand]["Total"].append(franchise)
        except:
            #print("Stage 1 failure (location: " + franchise + ")")
            try:
                franchiseBrands[franchiseBrand][franchiseFranchise] = [franchise]
                franchiseBrands[franchiseBrand]["Total"].append(franchise)
            except:
                #print("Stage 2 failure (location: " + franchise + ")")
                try:
                    franchiseBrands[franchiseBrand] = {franchiseFranchise: [franchise],"Total":[franchise]}
                except:
                    print("It broke!")

    franchiseBrandList = []
    for franchiseBrand in franchiseBrands.keys():
        franchiseBrandList.append(franchiseBrand)
    franchiseBrandList.sort()


    brandString = ""
    for brandName in franchiseBrandList:
        brandSet = brandName + ":\n"
        for franchiseName in franchiseBrands[brandName].keys():
            if franchiseName != "Total":
                brandSet = brandSet + "\t-" + franchiseName + " (" + str(len(franchiseBrands[brandName][franchiseName])) + "/" + str(len(franchiseBrands[brandName]["Total"])) + "): "
                for person in franchiseBrands[brandName][franchiseName]:
                    brandSet = brandSet + person + ", "
                brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandSet = brandSet + "\t-All " + " (" + str(len(franchiseBrands[brandName]["Total"])) + "/" + str(len(completedFranchises)) + "): "
        for person in franchiseBrands[brandName]["Total"]:
            brandSet = brandSet + person + ", "
        brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandString = brandString + "\n" + brandSet
        
    franchiseBrandsFile.write(brandString)

    inserts = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")
        searchFranchise = ""

        insertSearch = "Tara Strong"
        if franchiseInfo[7] != "":
            characterInsertList = franchiseInfo[7].split("|")
            for characterInsert in characterInsertList:
                if insertSearch == characterInsert:
                    print("Insert (Protagonist) Match: " + franchiseInfo[0] + " (" + franchise + ")")
                try:
                    inserts[characterInsert].append(franchise + " (protagonist)")
                except:
                    inserts[characterInsert] = [franchise + " (protagonist)"]
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")
        searchFranchise = ""

        insertSearch = "Tara Strong"
        if franchiseInfo[8] != "":
            characterInsertList = franchiseInfo[8].split("|")
            for characterInsert in characterInsertList:
                if insertSearch == characterInsert:
                    print("Insert (Antagonist) Match: " + franchiseInfo[0] + " (" + franchise + ")")
                try:
                    inserts[characterInsert].append(franchise + " (antagonist)")
                except:
                    inserts[characterInsert] = [franchise + " (antagonist)"]

    insertsPart2 = []
    for insert in inserts.keys():
        insertsPart2.append(insert)
    insertFile = open("Statistics\\Franchises\\inserts.txt", "w",encoding='utf8')
    insertFileByNumbers = open("Statistics\\Franchises\\inserts by numbers.txt", "w",encoding='utf8')

    insertsPart2.sort()
    for insert in insertsPart2:
        insertString = insert + " (" + str(len(inserts[insert])) + "): "
        for insertget in inserts[insert]:
            insertString = insertString + insertget + ", "
        insertString = insertString[0:len(insertString)-2:]
        insertFile.write(insertString + "\n")

    highNumber = -1
    for characterList in inserts.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    insertsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in inserts.keys():
            if len(inserts[characterList]) == x:
                try:
                    insertsByValues[x].append(characterList)
                except:
                    insertsByValues[x] = [characterList]


    for number in insertsByValues.keys():
        if number >= 2:
            for insert in insertsByValues[number]:
                
                insertString = insert + " (" + str(number) + "): "
                for franchise in inserts[insert]:
                    insertString = insertString + franchise + ", "
                insertString = insertString[0:len(insertString)-2:]
                insertFileByNumbers.write(insertString + "\n")

    inserts = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")
        searchFranchise = ""

        insertSearch = "Tara Strong"
        if franchiseInfo[7] != "":
            characterInsertList = franchiseInfo[7].split("|")
            for characterInsert in characterInsertList:
                if insertSearch == characterInsert:
                    print("Reverse insert (Protagonist) Match: " + characterInsert)
                try:
                    inserts[franchise].append(characterInsert + " (protagonist)")
                except:
                    inserts[franchise] = [characterInsert + " (protagonist)"]
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")
        searchFranchise = ""

        insertSearch = "Tara Strong"
        if franchiseInfo[8] != "":
            characterInsertList = franchiseInfo[8].split("|")
            for characterInsert in characterInsertList:
                if insertSearch == characterInsert:
                    print("Reverse insert (Antagonist) Match: " + characterInsert)
                try:
                    inserts[franchise].append(characterInsert + " (antagonist)")
                except:
                    inserts[franchise] = [characterInsert + " (antagonist)"]

    insertsPart2 = []
    for insert in inserts.keys():
        insertsPart2.append(insert)
    insertFile = open("Statistics\\Franchises\\reverse inserts.txt", "w",encoding='utf8')
    insertFileByNumbers = open("Statistics\\Franchises\\reverse inserts by numbers.txt", "w",encoding='utf8')

    insertsPart2.sort()
    for insert in insertsPart2:
        insertString = insert + " (" + str(len(inserts[insert])) + "): "
        for insertget in inserts[insert]:
            insertString = insertString + insertget + ", "
        insertString = insertString[0:len(insertString)-2:]
        insertFile.write(insertString + "\n")

    highNumber = -1
    for characterList in inserts.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    insertsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in inserts.keys():
            if len(inserts[characterList]) == x:
                try:
                    insertsByValues[x].append(characterList)
                except:
                    insertsByValues[x] = [characterList]


    for number in insertsByValues.keys():
        if number >= 2:
            for insert in insertsByValues[number]:
                
                insertString = insert + " (" + str(number) + "): "
                for franchise in inserts[insert]:
                    insertString = insertString + franchise + ", "
                insertString = insertString[0:len(insertString)-2:]
                insertFileByNumbers.write(insertString + "\n")

    mediums = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")

        mediumSearch = "----"
        if franchiseInfo[13] != "":
            mediumList = franchiseInfo[13].split(",")
            for medium in mediumList:
                if mediumSearch == medium:
                    print("Mediums Match: " + franchiseInfo[0] + " (" + franchise + ")")
                try:
                    mediums[medium].append(franchise)
                except:
                    mediums[medium] = [franchise]
                    
                #else:
                    #print(franchiseInfo[0] + " already expended " + characterTag)

    mediumsPart2 = []
    for medium in mediums.keys():
        mediumsPart2.append(medium)
    mediumFile = open("Statistics\\Franchises\\mediums.txt", "w",encoding='utf8')
    mediumFileByNumbers = open("Statistics\\Franchises\\mediums by numbers.txt", "w",encoding='utf8')

    mediumsPart2.sort()
    for medium in mediumsPart2:
        mediumString = medium + " (" + str(len(mediums[medium])) + "): "
        for medyum in mediums[medium]:
            mediumString = mediumString + medyum + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        mediumFile.write(mediumString + "\n")

    highNumber = -1
    for characterList in mediums.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    mediumByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in mediums.keys():
            if len(mediums[characterList]) == x:
                try:
                    mediumByValues[x].append(characterList)
                except:
                    mediumByValues[x] = [characterList]


    for number in mediumByValues.keys():
        for medium in mediumByValues[number]:
            mediumString = medium + " (" + str(number) + "): "
            for franchise in mediums[medium]:
                mediumString = mediumString + franchise + ", "
            mediumString = mediumString[0:len(mediumString)-2:]
            mediumFileByNumbers.write(mediumString + "\n")

    colors = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")

        colorSearch = "-----"
        color = franchiseInfo[14]
        if colorSearch == color:
            print("Color Match: " + franchiseInfo[0] + " (" + franchise + ")")
        try:
            colors[color].append(franchise)
        except:
            colors[color] = [franchise]
                    
                #else:
                    #print(franchiseInfo[0] + " already expended " + characterTag)

    colorPart2 = []
    for color in colors.keys():
        colorPart2.append(color)
    colorFile = open("Statistics\\Franchises\\color.txt", "w",encoding='utf8')
    colorFileByNumbers = open("Statistics\\Franchises\\color by numbers.txt", "w",encoding='utf8')

    colorPart2.sort()
    for color in colorPart2:
        colorString = color + " (" + str(len(colors[color])) + "): "
        for colour in colors[color]:
            colorString = colorString + colour + ", "
        colorString = colorString[0:len(colorString)-2:]
        colorFile.write(colorString + "\n")

    highNumber = -1
    for characterList in colors.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    colorByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in colors.keys():
            if len(colors[characterList]) == x:
                try:
                    colorByValues[x].append(characterList)
                except:
                    colorByValues[x] = [characterList]


    for number in colorByValues.keys():
        if number >= 2:
            for color in colorByValues[number]:
                colorString = color + " (" + str(number) + "): "
                for franchise in colors[color]:
                    colorString = colorString + franchise + ", "
                colorString = colorString[0:len(colorString)-2:]
                colorFileByNumbers.write(colorString + "\n")

    powerLevels = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")

        powerLevelSearch = "----"
        powerLevel = franchiseInfo[16]
        if powerLevelSearch == powerLevel:
            print("Power Level Match: " + franchiseInfo[0] + " (" + franchise + ")")
        try:
            powerLevels[powerLevel].append(franchise)
        except:
            powerLevels[powerLevel] = [franchise]
                    
                #else:
                    #print(franchiseInfo[0] + " already expended " + characterTag)

    powerLevelsPart2 = []
    for powerLevel in powerLevels.keys():
        powerLevelsPart2.append(powerLevel)
    powerLevelsFile = open("Statistics\\Franchises\\power levels.txt", "w",encoding='utf8')
    powerLevelFileByNumbers = open("Statistics\\Franchises\\power levels by numbers.txt", "w",encoding='utf8')

    powerLevelsPart2.sort()
    for powerLevel in powerLevelsPart2:
        powerLevelString = powerLevel + " (" + str(len(powerLevels[powerLevel])) + "): "
        for pwrlvl in powerLevels[powerLevel]:
            powerLevelString = powerLevelString + pwrlvl + ", "
        powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
        powerLevelsFile.write(powerLevelString + "\n")

    highNumber = -1
    for characterList in powerLevels.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    powerLevelByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in powerLevels.keys():
            if len(powerLevels[characterList]) == x:
                try:
                    powerLevelByValues[x].append(characterList)
                except:
                    powerLevelByValues[x] = [characterList]


    for number in powerLevelByValues.keys():
        for powerLevel in powerLevelByValues[number]:
            powerLevelString = powerLevel + " (" + str(number) + "): "
            for franchise in powerLevels[powerLevel]:
                powerLevelString = powerLevelString + franchise + ", "
            powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
            powerLevelFileByNumbers.write(powerLevelString + "\n")

    popularities = {}
    for franchise in completedFranchises:
        firstLetter = franchise[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        franchiseFile = open("Franchises\\" + firstLetter + "\\" + franchise + ".txt", "r", encoding='utf8')
        franchiseInfo = franchiseFile.read().split("\n")

        popularitySearch = "-----"
        popularity = franchiseInfo[15]
        if popularitySearch == popularity:
            print("Popularity Match: " + franchiseInfo[0] + " (" + franchise + ")")
        try:
            popularities[popularity].append(franchise)
        except:
            popularities[popularity] = [franchise]
                    
                #else:
                    #print(franchiseInfo[0] + " already expended " + characterTag)

    popularityPart2 = []
    for popularity in popularities.keys():
        popularityPart2.append(popularity)
    popularityFile = open("Statistics\\Franchises\\popularity.txt", "w",encoding='utf8')
    popularityFileByNumbers = open("Statistics\\Franchises\\popularity by numbers.txt", "w",encoding='utf8')

    popularityPart2.sort()
    for popularity in popularityPart2:
        popularityString = popularity + " (" + str(len(popularities[popularity])) + "): "
        for popu in popularities[popularity]:
            popularityString = popularityString + popu + ", "
        popularityString = popularityString[0:len(popularityString)-2:]
        popularityFile.write(popularityString + "\n")

    highNumber = -1
    for characterList in popularities.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    popularityByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in popularities.keys():
            if len(popularities[characterList]) == x:
                try:
                    popularityByValues[x].append(characterList)
                except:
                    popularityByValues[x] = [characterList]


    for number in popularityByValues.keys():
        for popularity in popularityByValues[number]:
            popularityString = popularity + " (" + str(number) + "): "
            for franchise in popularities[popularity]:
                popularityString = popularityString + franchise + ", "
            popularityString = popularityString[0:len(popularityString)-2:]
            popularityFileByNumbers.write(popularityString + "\n")

    #Power Levels, Popularities
    print("Completed Franchise Updates!")