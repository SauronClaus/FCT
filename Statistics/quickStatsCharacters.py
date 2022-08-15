# This program fills out all of the files under Statistics\\Characters

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os
def quickStatsCharacters():
    completedCharacters = []
    undoneCharacters = []
    needToUpdateCharacters = []
    weirdCharacters = []
    allCharacters = []

    # List all files in a directory using os.listdir
    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 30:
                    weird = False
                    for lineNum in range(len(characterInfo)):
                        line = characterInfo[lineNum]
                        if line[0:1:] in numbers and lineNum != 9 and line != "2K Games" and line != "39 Clues" and line != "20th Century Fox":
                            weird = True
                            weirdCharacters.append(entry[0:len(entry)-4:])
                            print("Check:" + entry[0:len(entry)-4:])
                    if weird == False:
                        completedCharacters.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 5:
                        undoneCharacters.append(entry[0:len(entry)-4:])
                    else:
                        if len(characterInfo) == 17 or len(characterInfo) == 22 or len(characterInfo) == 24 or len(characterInfo) == 29:
                            needToUpdateCharacters.append(entry[0:len(entry)-4:])
                        else:
                            weirdCharacters.append(entry[0:len(entry)-4:])
                allCharacters.append(entry[0:len(entry)-4:])
                #if characterInfo[0] != entry[0:len(entry)-4:]:
                    #print("Check " + characterInfo[0] + " (" + entry[0:len(entry)-4:] + ")")

    # Stats: 
        # Numbers (total % complete)
        # Theme Song (have vs not)
        # Signature Weapon (have vs not)

    # Brand and Franchise

    # Names (First & Last) (Shared only)
    # Actors (Both)
    # Age (years and decades) (Both)
    # Types (Both)
    # Race (Both)
    # Alignment (Both)
    # Role (Both)
    # Gender (Both)
    # Tags (Both)- use tiedTags
    # Power Level (Both)
    # Popularity
    # Groups
    # Medium
    # Color

    statsFile = open("Statistics\\Characters\\stats.txt", "w",encoding='utf8')

    quickStatNum = str(len(completedCharacters)) + " (completed)/" + str(len(needToUpdateCharacters)) + " (need to update)/" + str(len(undoneCharacters)) + " (incomplete)/" + str(len(weirdCharacters)) + " (weird)/Total:" + str(len(allCharacters))

    themeSongs = 0
    sigWeapons = 0

    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")
        if characterInfo[19] != "":
            themeSongs+=1
        if characterInfo[22] != "":
            sigWeapons+=1

    themeSongString = "Theme Songs: " + str(themeSongs) + "/" + str(len(completedCharacters))
    sigWeaponsString = "Signature Weapons: " + str(sigWeapons) + "/" + str(len(completedCharacters))

    finalStats = quickStatNum + "\n" + themeSongString + "\n" + sigWeaponsString
    statsFile.write(finalStats)

    brands = {}
    brandsFile = open("Statistics\\Characters\\brands.txt", "w",encoding='utf8')

    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        searchFranchise = ""

        characterBrand = characterInfo[21]
        characterFranchise = characterInfo[1]
        if characterFranchise == searchFranchise:
            print("-" + characterInfo[0] + " (" + character + ") is in " + characterBrand + " (Brand)/" + characterFranchise + " (Franchise)")
        try:
            brands[characterBrand][characterFranchise].append(character)
            brands[characterBrand]["Total"].append(character)
        except:
            #print("Stage 1 failure (location: " + character + ")")
            try:
                brands[characterBrand][characterFranchise] = [character]
                brands[characterBrand]["Total"].append(character)
            except:
                #print("Stage 2 failure (location: " + character + ")")
                try:
                    brands[characterBrand] = {characterFranchise: [character],"Total":[character]}
                except:
                    print("It broke!")

    brandString = ""
    for brandName in brands.keys():
        brandSet = brandName + ":\n"
        for franchiseName in brands[brandName].keys():
            if franchiseName != "Total":
                brandSet = brandSet + "\t-" + franchiseName + " (" + str(len(brands[brandName][franchiseName])) + "/" + str(len(brands[brandName]["Total"])) + "): "
                for person in brands[brandName][franchiseName]:
                    brandSet = brandSet + person + ", "
                brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandSet = brandSet + "\t-All " + " (" + str(len(brands[brandName]["Total"])) + "/" + str(len(completedCharacters)) + "): "
        for person in brands[brandName]["Total"]:
            brandSet = brandSet + person + ", "
        brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandString = brandString + "\n" + brandSet
        
    brandsFile.write(brandString)

    firstNames = {}
    lastNames = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        firstNameSearch = "------"
        characterFirstName = characterInfo[5]
        if firstNameSearch == characterFirstName:
            print("First Name Search: " + characterInfo[0] + " (" + character + ")")

        lastNameSearch = "aaaaaa"
        characterLastName = characterInfo[6]
        if lastNameSearch == characterLastName:
            print("Last Name Search: " + characterInfo[0] + " (" + character + ")")

        if characterFirstName != "":
            try:
                firstNames[characterFirstName].append(character)
            except:
                firstNames[characterFirstName] = [character]
        if characterLastName != "":
            try:
                lastNames[characterLastName].append(character)
            except:
                lastNames[characterLastName] = [character]

    firstNameFile = open("Statistics\\Characters\\firstNames.txt", "w",encoding='utf8')
    lastNameFile = open("Statistics\\Characters\\lastNames.txt", "w",encoding='utf8')
    lastNamesByNumbers = open("Statistics\\Characters\\lastNamesByNumbers.txt", "w", encoding='utf8')
    firstNamesByNumbers = open("Statistics\\Characters\\firstNamesByNumbers.txt", "w", encoding='utf8')

    for firstName in firstNames.keys():
        if len(firstNames[firstName]) >= 2:
            firstNameString = firstName + ": "
            for person in firstNames[firstName]:
                firstNameString = firstNameString + person + ", "
            firstNameString = firstNameString[0:len(firstNameString)-2:]
            firstNameFile.write(firstNameString + "\n")
    for lastName in lastNames.keys():
        if len(lastNames[lastName]) >= 2:
            lastNameString = lastName + ": "
            for person in lastNames[lastName]:
                lastNameString = lastNameString + person + ", "
            lastNameString = lastNameString[0:len(lastNameString)-2:]
            lastNameFile.write(lastNameString + "\n")

    highNumber = -1
    for characterList in lastNames.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    typesByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in lastNames.keys():
            if len(lastNames[characterList]) == x:
                try:
                    typesByValues[x].append(characterList)
                except:
                    typesByValues[x] = [characterList]

    for number in typesByValues.keys():
        for typeName in typesByValues[number]:
            typeString = typeName + " (" + str(number) + "): "
            for character in lastNames[typeName]:
                typeString = typeString + character + ", "
            typeString = typeString[0:len(typeString)-2:]
            lastNamesByNumbers.write(typeString + "\n")

    highNumber = -1
    for characterList in firstNames.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    typesByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in firstNames.keys():
            if len(firstNames[characterList]) == x:
                try:
                    typesByValues[x].append(characterList)
                except:
                    typesByValues[x] = [characterList]

    for number in typesByValues.keys():
        for typeName in typesByValues[number]:
            typeString = typeName + " (" + str(number) + "): "
            for character in firstNames[typeName]:
                typeString = typeString + character + ", "
            typeString = typeString[0:len(typeString)-2:]
            firstNamesByNumbers.write(typeString + "\n")

    actors = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        actorSearch = "-----"
        if characterInfo[8] != "":
            characterActorList = characterInfo[8].split("|")
            for characterActor in characterActorList:
                if actorSearch == characterActor:
                    print("Actor Match: " + characterInfo[0] + " (" + character + ")")

                try:
                    actors[characterActor].append(character)
                except:
                    actors[characterActor] = [character]

    actorPart2 = []
    for actor in actors.keys():
        actorPart2.append(actor)
    actorFile = open("Statistics\\Characters\\actors.txt", "w",encoding='utf8')
    actorFileByNumber = open("Statistics\\Characters\\actorsByNumbers.txt", "w",encoding='utf8')

    actorPart2.sort()

    highNumber = -1
    for characterList in actors.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    actorsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in actors.keys():
            if len(actors[characterList]) == x:
                try:
                    actorsByValues[x].append(characterList)
                except:
                    actorsByValues[x] = [characterList]

    for actor in actorPart2:
        if len(actors[actor]) >= 2:
            actorString = actor + " (" + str(len(actors[actor])) + "): "
            for character in actors[actor]:
                actorString = actorString + character + ", "
            actorString = actorString[0:len(actorString)-2:]
            actorFile.write(actorString + "\n")

    for number in actorsByValues.keys():
        for actorName in actorsByValues[number]:
            if len(actors[actorName]) >= 2:
                actorString = actorName + " (" + str(number) + "): "
                for character in actors[actorName]:
                    actorString = actorString + character + ", "
                actorString = actorString[0:len(actorString)-2:]
                actorFileByNumber.write(actorString + "\n")

    years = {}
    decades = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")
        if characterInfo[9] != "":
            yearSearch = ""
            characterYear = characterInfo[9].split("|")[0]
            if yearSearch == characterYear:
                print("Year Search: " + characterInfo[0] + " (" + character + ")")

            decadeSearch = ""
            characterDecade = characterInfo[9].split("|")[1]
            if decadeSearch == characterDecade:
                print("Decades Search: " + characterInfo[0] + " (" + character + ")")

            try:
                years[characterYear].append(character)
            except:
                years[characterYear] = [character]
            try:
                decades[characterDecade].append(character)
            except:
                decades[characterDecade] = [character]

    yearFile = open("Statistics\\Characters\\years.txt", "w",encoding='utf8')
    decadesFile = open("Statistics\\Characters\\decades.txt", "w",encoding='utf8')\

    yearsPart2 = []
    for year in years.keys():
        yearsPart2.append(int(year))

    decadesPart2 = []
    for decade in decades.keys():
        decadesPart2.append(int(decade))

    yearsPart2.sort()
    decadesPart2.sort()
    for year in yearsPart2:
        yearString = str(year) + " (" + str(len(years[str(year)])) + "): "
        for character in years[str(year)]:
            yearString = yearString + character + ", "
        yearString = yearString[0:len(yearString)-2:]
        yearFile.write(yearString + "\n")
    for decade in decadesPart2:
        decadeString = str(decade) + " (" + str(len(decades[str(decade)])) + "): "
        for character in decades[str(decade)]:
            decadeString = decadeString + character + ", "
        decadeString = decadeString[0:len(decadeString)-2:]
        decadesFile.write(decadeString + "\n")


    types = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        typeSearch = "Tara Strong"
        if characterInfo[10] != "":
            characterType = characterInfo[10]
            if typeSearch == characterType:
                print("Type Match: " + characterInfo[0] + " (" + character + ")")

            try:
                types[characterType].append(character)
            except:
                types[characterType] = [character]

    typesPart2 = []
    for typeIt in types.keys():
        typesPart2.append(typeIt)
    typeFile = open("Statistics\\Characters\\types.txt", "w",encoding='utf8')
    typeFileByNumbers = open("Statistics\\Characters\\typesByNumbers.txt", "w",encoding='utf8')

    typesPart2.sort()
    for typeIt in typesPart2:
        typeString = typeIt + " (" + str(len(types[typeIt])) + "): "
        for typein in types[typeIt]:
            typeString = typeString + typein + ", "
        typeString = typeString[0:len(typeString)-2:]
        typeFile.write(typeString + "\n")

    highNumber = -1
    for characterList in types.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    typesByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in types.keys():
            if len(types[characterList]) == x:
                try:
                    typesByValues[x].append(characterList)
                except:
                    typesByValues[x] = [characterList]


    for number in typesByValues.keys():
        for typeName in typesByValues[number]:
            typeString = typeName + " (" + str(number) + "): "
            for character in types[typeName]:
                typeString = typeString + character + ", "
            typeString = typeString[0:len(typeString)-2:]
            typeFileByNumbers.write(typeString + "\n")
    races = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        raceSearch = "Tara Strong"
        if characterInfo[11] != "":
            characterRace = characterInfo[11]
            if raceSearch == characterRace:
                print("Type Match: " + characterInfo[0] + " (" + character + ")")

            try:
                races[characterRace].append(character)
            except:
                races[characterRace] = [character]

    racesPart2 = []
    for race in races.keys():
        racesPart2.append(race)
    raceFile = open("Statistics\\Characters\\races.txt", "w",encoding='utf8')
    raceFileByNumber = open("Statistics\\Characters\\racesByNumbers.txt", "w",encoding='utf8')

    racesPart2.sort()
    for race in racesPart2:
        raceString = race + " (" + str(len(races[race])) + "): "
        for racer in races[race]:
            raceString = raceString + racer + ", "
        raceString = raceString[0:len(raceString)-2:]
        raceFile.write(raceString + "\n")

    highNumber = -1
    for characterList in races.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    racesByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in races.keys():
            if len(races[characterList]) == x:
                try:
                    racesByValues[x].append(characterList)
                except:
                    racesByValues[x] = [characterList]


    for number in racesByValues.keys():
        for race in racesByValues[number]:
            raceString = race + " (" + str(number) + "): "
            for character in races[race]:
                raceString = raceString + character + ", "
            raceString = raceString[0:len(raceString)-2:]
            raceFileByNumber.write(raceString + "\n")

    alignments = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        alignmentSearch = "Tara Strong"
        if characterInfo[12] != "":
            characterAlignment = characterInfo[12]
            if alignmentSearch == characterAlignment:
                print("Type Match: " + characterInfo[0] + " (" + character + ")")

            try:
                alignments[characterAlignment].append(character)
            except:
                alignments[characterAlignment] = [character]

    alignmentsPart2 = []
    for alignment in alignments.keys():
        alignmentsPart2.append(alignment)
    alignmentFile = open("Statistics\\Characters\\alignments.txt", "w",encoding='utf8')
    alignmentsPart2.sort()
    for alignment in alignmentsPart2:
        alignString = alignment + " (" + str(len(alignments[alignment])) + "): "
        for character in alignments[alignment]:
            alignString = alignString + character + ", "
        alignString = alignString[0:len(alignString)-2:]
        alignmentFile.write(alignString + "\n")

    roles = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        roleSearch = "Tara Strong"
        if characterInfo[13] != "":
            characterRole = characterInfo[13]
            if roleSearch == characterRole:
                print("Type Match: " + characterInfo[0] + " (" + character + ")")

            try:
                roles[characterRole].append(character)
            except:
                roles[characterRole] = [character]

    rolesPart2 = []
    for role in roles.keys():
        rolesPart2.append(role)
    roleFile = open("Statistics\\Characters\\roles.txt", "w",encoding='utf8')
    roleFileByNumber = open("Statistics\\Characters\\rolesByNumbers.txt", "w",encoding='utf8')
    rolesPart2.sort()

    for role in rolesPart2:
        roleString = role + " (" + str(len(roles[role])) + "): "
        for rolen in roles[role]:
            roleString = roleString + rolen + ", "
        roleString = roleString[0:len(roleString)-2:]
        roleFile.write(roleString + "\n")

    highNumber = -1
    for characterList in roles.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    rolesByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in roles.keys():
            if len(roles[characterList]) == x:
                try:
                    rolesByValues[x].append(characterList)
                except:
                    rolesByValues[x] = [characterList]


    for number in rolesByValues.keys():
        for role in rolesByValues[number]:
            roleString = role + " (" + str(number) + "): "
            for character in roles[role]:
                roleString = roleString + character + ", "
            roleString = roleString[0:len(roleString)-2:]
            roleFileByNumber.write(roleString + "\n")

    genders = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        genderSearch = "----"
        if characterInfo[14] != "":
            characterGender = characterInfo[14]
            if genderSearch == characterGender:
                print("Gender Match: " + characterInfo[0] + " (" + character + ")")

            try:
                genders[characterGender].append(character)
            except:
                genders[characterGender] = [character]

    gendersPart2 = []
    for gender in genders.keys():
        gendersPart2.append(gender)
    genderFile = open("Statistics\\Characters\\genders.txt", "w",encoding='utf8')
    gendersPart2.sort()
    for gender in gendersPart2:
        genderString = gender + " (" + str(len(genders[gender])) + "): "
        for gendered in genders[gender]:
            genderString = genderString + gendered + ", "
        genderString = genderString[0:len(genderString)-2:]
        genderFile.write(genderString + "\n")

    powerLevels = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        powerLevelSearch = "-----"
        if characterInfo[16] != "":
            characterPowerLevel = characterInfo[16]
            if powerLevelSearch == characterPowerLevel:
                print("Power Level Match: " + characterInfo[0] + " (" + character + ")")

            try:
                powerLevels[characterPowerLevel].append(character)
            except:
                powerLevels[characterPowerLevel] = [character]

    powerLevelsPart2 = []
    for powerLevel in powerLevels.keys():
        powerLevelsPart2.append(powerLevel)
    powerLevelsFile = open("Statistics\\Characters\\power levels.txt", "w",encoding='utf8')
    powerLevelsFileByNumbers = open("Statistics\\Characters\\power levels by numbers.txt", "w",encoding='utf8')

    powerLevelsPart2.sort()

    for powerLevel in powerLevelsPart2:
        powerLevelString = powerLevel + " (" + str(len(powerLevels[powerLevel])) + "): "
        for powerLVL in powerLevels[powerLevel]:
            powerLevelString = powerLevelString + powerLVL + ", "
        powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
        powerLevelsFile.write(powerLevelString + "\n")

    highNumber = -1
    for characterList in powerLevels.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    powerLevelsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in powerLevels.keys():
            if len(powerLevels[characterList]) == x:
                try:
                    powerLevelsByValues[x].append(characterList)
                except:
                    powerLevelsByValues[x] = [characterList]


    for number in powerLevelsByValues.keys():
        for powerLevel in powerLevelsByValues[number]:
            powerLevelString = powerLevel + " (" + str(number) + "): "
            for character in powerLevels[powerLevel]:
                powerLevelString = powerLevelString + character + ", "
            powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
            powerLevelsFileByNumbers.write(powerLevelString + "\n")

    popularities = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        popularitySearch = "Tara Strong"
        if characterInfo[17] != "":
            characterPopularity = characterInfo[17]
            if popularitySearch == characterPopularity:
                print("Popularity Match: " + characterInfo[0] + " (" + character + ")")

            try:
                popularities[characterPopularity].append(character)
            except:
                popularities[characterPopularity] = [character]

    popularitiesPart2 = []
    for popularity in popularities.keys():
        popularitiesPart2.append(popularity)
    popularitiesFile = open("Statistics\\Characters\\popularities.txt", "w",encoding='utf8')
    popularitiesPart2.sort()
    for popularity in popularities:
        popularityString = popularity + " (" + str(len(popularities[popularity])) + "): "
        for character in popularities[popularity]:
            popularityString = popularityString + character + ", "
        popularityString = popularityString[0:len(popularityString)-2:]
        popularitiesFile.write(popularityString + "\n")

    mediums = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        mediumSearch = "Tara Strong"
        if characterInfo[20] != "":
            characterMediumList = characterInfo[20].split(",")
            for characterMedium in characterMediumList:
                if mediumSearch == characterMedium:
                    print("Medium Match: " + characterInfo[0] + " (" + character + ")")

                try:
                    mediums[characterMedium].append(character)
                except:
                    mediums[characterMedium] = [character]

    mediumsPart2 = []
    for medium in mediums.keys():
        mediumsPart2.append(medium)
    mediumsFile = open("Statistics\\Characters\\mediums.txt", "w",encoding='utf8')
    mediumsFileByNumbers = open("Statistics\\Characters\\mediums by numbers.txt", "w",encoding='utf8')

    mediumsPart2.sort()

    for medium in mediumsPart2:
        mediumString = medium + " (" + str(len(mediums[medium])) + "): "
        for mediumed in mediums[medium]:
            mediumString = mediumString + mediumed + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        mediumsFile.write(mediumString + "\n")

    highNumber = -1
    for characterList in mediums.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    mediumsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in mediums.keys():
            if len(mediums[characterList]) == x:
                try:
                    mediumsByValues[x].append(characterList)
                except:
                    mediumsByValues[x] = [characterList]


    for number in mediumsByValues.keys():
        for medium in mediumsByValues[number]:
            mediumString = medium + " (" + str(number) + "): "
            for character in mediums[medium]:
                mediumString = mediumString + character + ", "
            mediumString = mediumString[0:len(mediumString)-2:]
            mediumsFileByNumbers.write(mediumString + "\n")

    colors = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        colorSearch = "Tara Strong"
        if characterInfo[23] != "":
            characterColor = characterInfo[23]
            if colorSearch == characterColor:
                print("Color Match: " + characterInfo[0] + " (" + character + ")")

            try:
                colors[characterColor].append(character)
            except:
                colors[characterColor] = [character]

    colorsPart2 = []
    for color in colors.keys():
        colorsPart2.append(color)
    colorFile = open("Statistics\\Characters\\colors.txt", "w",encoding='utf8')
    colorsFileByNumbers= open("Statistics\\Characters\\colors by numbers.txt", "w",encoding='utf8')
    colorsPart2.sort()
    for color in colorsPart2:
        colorString = color + " (" + str(len(colors[color])) + "): "
        for colour in colors[color]:
            colorString = colorString + colour + ", "
        colorString = colorString[0:len(colorString)-2:]
        colorFile.write(colorString + "\n")

    highNumber = -1
    for characterList in colors.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    colorsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in colors.keys():
            if len(colors[characterList]) == x:
                try:
                    colorsByValues[x].append(characterList)
                except:
                    colorsByValues[x] = [characterList]


    for number in colorsByValues.keys():
        for color in colorsByValues[number]:
            colorString = color + " (" + str(number) + "): "
            for character in colors[color]:
                colorString = colorString + character + ", "
            colorString = colorString[0:len(colorString)-2:]
            colorsFileByNumbers.write(colorString + "\n")



    groups = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        groupSearch = "Tara Strong"
        if characterInfo[18] != "":
            characterGroupList = characterInfo[18].split(",")
            for characterGroup in characterGroupList:
                if groupSearch == characterGroup:
                    print("Medium Match: " + characterInfo[0] + " (" + character + ")")

                try:
                    groups[characterGroup].append(character)
                except:
                    groups[characterGroup] = [character]

    groupsPart2 = []
    for group in groups.keys():
        groupsPart2.append(group)
    groupFile = open("Statistics\\Characters\\groups.txt", "w",encoding='utf8')
    groupFileByNumbers = open("Statistics\\Characters\\groups by numbers.txt", "w",encoding='utf8')

    groupsPart2.sort()
    for group in groupsPart2:
        groupString = group + " (" + str(len(groups[group])) + "): "
        for groupem in groups[group]:
            groupString = groupString + groupem + ", "
        groupString = groupString[0:len(groupString)-2:]
        groupFile.write(groupString + "\n")

    highNumber = -1
    for characterList in groups.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    groupsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in groups.keys():
            if len(groups[characterList]) == x:
                try:
                    groupsByValues[x].append(characterList)
                except:
                    groupsByValues[x] = [characterList]


    for number in groupsByValues.keys():
        for group in groupsByValues[number]:
            groupString = group + " (" + str(number) + "): "
            for character in groups[group]:
                groupString = groupString + character + ", "
            groupString = groupString[0:len(groupString)-2:]
            groupFileByNumbers.write(groupString + "\n")

    tags = {}
    for character in completedCharacters:
        firstLetter = character[0:1:]
        if firstLetter in numbers:
            firstLetter = "#"
        tagsExpended = []
        characterFile = open("Characters\\" + firstLetter + "\\" + character + ".txt", "r", encoding='utf8')
        characterInfo = characterFile.read().split("\n")

        tagSearch = "Tara Strong"
        if characterInfo[15] != "":
            characterTagList = characterInfo[15].split(",")
            for characterTagFull in characterTagList:
                characterTag = characterTagFull.split("|")
                if tagSearch == characterTag[0]:
                    print("Tag Match: " + characterInfo[0] + " (" + character + ")")
                if not (characterTag[0] in tagsExpended):
                    if len(characterTag) >= 2:
                        try:
                            tags[characterTag[0]].append(character + " (" + characterTag[1] + ")")
                        except:
                            tags[characterTag[0]] = [character + " (" + characterTag[1] + ")"]
                    else:
                        try:
                            tags[characterTag[0]].append(character)
                        except:
                            tags[characterTag[0]] = [character]
                    tagsExpended.append(characterTag[0])
                #else:
                    #print(characterInfo[0] + " already expended " + characterTag)

    tagsPart2 = []
    for tag in tags.keys():
        tagsPart2.append(tag)
    tagFile = open("Statistics\\Characters\\tags.txt", "w",encoding='utf8')
    tagFileByNumbers = open("Statistics\\Characters\\tags by numbers.txt", "w",encoding='utf8')

    tagsPart2.sort()
    for tag in tagsPart2:
        tagString = tag + " (" + str(len(tags[tag])) + "): "
        for tagget in tags[tag]:
            tagString = tagString + tagget + ", "
        tagString = tagString[0:len(tagString)-2:]
        tagFile.write(tagString + "\n")

    highNumber = -1
    for characterList in tags.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    tagsByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in tags.keys():
            if len(tags[characterList]) == x:
                try:
                    tagsByValues[x].append(characterList)
                except:
                    tagsByValues[x] = [characterList]


    for number in tagsByValues.keys():
        for tag in tagsByValues[number]:
            tagString = tag + " (" + str(number) + "): "
            for character in tags[tag]:
                tagString = tagString + character + ", "
            tagString = tagString[0:len(tagString)-2:]
            tagFileByNumbers.write(tagString + "\n")

    print("Completed Characters Updates!")


quickStatsCharacters()