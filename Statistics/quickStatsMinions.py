# This program fills out all of the quick stat files inside the folder Statistics\\Minions

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

def quickStatsMinions():
    completedMinions = []
    undoneMinions = []
    needToUpdateMinions = []
    weirdMinions = []
    allMinions = []

    basepath = "Minions"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            MinionsFile = open(basepath + "/" + entry, "r", encoding='utf8')
            MinionsInfo = MinionsFile.read().split("\n")
            if entry != "readMe.txt":
                if len(MinionsInfo) == 24:
                    completedMinions.append(entry[0:len(entry)-4:])
                else:
                    if len(MinionsInfo) == 0:
                        needToUpdateMinions.append(entry[0:len(entry)-4:])
                    else:
                        if len(MinionsInfo) == -1:
                            undoneMinions.append(entry[0:len(entry)-4:])
                        else:
                            weirdMinions.append(entry[0:len(entry)-4:])
                allMinions.append(entry[0:len(entry)-4:])

    completedMinions.sort()
    undoneMinions.sort()
    needToUpdateMinions.sort()
    weirdMinions.sort()
    allMinions.sort()

    statsFile = open("Statistics\\Minions\\stats.txt", "w",encoding='utf8')
    quickStatNum = str(len(completedMinions)) + " (completed)/" + str(len(needToUpdateMinions)) + " (need to update)/" + str(len(undoneMinions)) + " (incompleted)/" + str(len(weirdMinions)) + " (weird)/Total: " + str(len(allMinions))
    statsFile.write(quickStatNum)

    minionsBrands = {}
    minionsBrandsFile = open("Statistics\\Minions\\minionsBrands.txt", "w",encoding='utf8')

    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")
        searchFranchise = ""

        minionsBrand = minionsInfo[17]
        minionsFranchise = minionsInfo[1]
        if minionsFranchise == searchFranchise:
            print("-" + minionsInfo[0] + " (" + minions + ") is in " + minionsBrand + ": " + minionsFranchise + " (Franchise)")
        try:
            minionsBrands[minionsBrand][minionsFranchise].append(minions)
            minionsBrands[minionsBrand]["Total"].append(minions)
        except:
            #print("Stage 1 failure (location: " + minions + ")")
            try:
                minionsBrands[minionsBrand][minionsFranchise] = [minions]
                minionsBrands[minionsBrand]["Total"].append(minions)
            except:
                #print("Stage 2 failure (location: " + minions + ")")
                try:
                    minionsBrands[minionsBrand] = {minionsFranchise: [minions],"Total":[minions]}
                except:
                    print("It broke!")

    minionsBrandList = []
    for minionsBrand in minionsBrands.keys():
        minionsBrandList.append(minionsBrand)
    minionsBrandList.sort()


    brandString = ""
    for brandName in minionsBrandList:
        brandSet = brandName + ":\n"
        for franchiseName in minionsBrands[brandName].keys():
            if franchiseName != "Total":
                brandSet = brandSet + "\t-" + franchiseName + " (" + str(len(minionsBrands[brandName][franchiseName])) + "/" + str(len(minionsBrands[brandName]["Total"])) + "): "
                for person in minionsBrands[brandName][franchiseName]:
                    brandSet = brandSet + person + ", "
                brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandSet = brandSet + "\t-All " + " (" + str(len(minionsBrands[brandName]["Total"])) + "/" + str(len(completedMinions)) + "): "
        for person in minionsBrands[brandName]["Total"]:
            brandSet = brandSet + person + ", "
        brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandString = brandString + "\n" + brandSet
        
    minionsBrandsFile.write(brandString)

    tags = {}
    for minions in completedMinions:
        tagsExpended = []
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        tagSearch = "Tara Strong"
        if minionsInfo[12] != "":
            characterTagList = minionsInfo[12].split(",")
            for characterTagFull in characterTagList:
                characterTag = characterTagFull.split("|")
                if tagSearch == characterTag[0]:
                    print("Tag Match: " + minionsInfo[0] + " (" + minions + ")")
                if not (characterTag[0] in tagsExpended):
                    if len(characterTag) >= 2:
                        try:
                            tags[characterTag[0]].append(minions + " (" + characterTag[1] + ")")
                        except:
                            tags[characterTag[0]] = [minions + " (" + characterTag[1] + ")"]
                    else:
                        try:
                            tags[characterTag[0]].append(minions)
                        except:
                            tags[characterTag[0]] = [minions]
                    tagsExpended.append(characterTag[0])
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    tagsPart2 = []
    for tag in tags.keys():
        tagsPart2.append(tag)
    tagFile = open("Statistics\\Minions\\tags.txt", "w",encoding='utf8')
    tagFileByNumbers = open("Statistics\\Minions\\tags by numbers.txt", "w",encoding='utf8')

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
            for minions in tags[tag]:
                tagString = tagString + minions + ", "
            tagString = tagString[0:len(tagString)-2:]
            tagFileByNumbers.write(tagString + "\n")
    
    commanders = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        commanderSearch = "---"
        if minionsInfo[5] != "":
            commanderList = minionsInfo[5].split("|")
            for commander in commanderList:
                if commanderSearch == commander:
                    print("Commanders Match: " + minionsInfo[0] + " (" + minions + ")")
                try:
                    commanders[commander].append(minions)
                except:
                    commanders[commander] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    commandersPart2 = []
    for commander in commanders.keys():
        commandersPart2.append(commander)
    commanderFile = open("Statistics\\Minions\\commanders.txt", "w",encoding='utf8')
    commanderFileByNumbers = open("Statistics\\Minions\\commanders by numbers.txt", "w",encoding='utf8')

    commandersPart2.sort()
    for commander in commandersPart2:
        commanderString = commander + " (" + str(len(commanders[commander])) + "): "
        for wielden in commanders[commander]:
            commanderString = commanderString + wielden + ", "
        commanderString = commanderString[0:len(commanderString)-2:]
        commanderFile.write(commanderString + "\n")

    highNumber = -1
    for characterList in commanders.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    commanderByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in commanders.keys():
            if len(commanders[characterList]) == x:
                try:
                    commanderByValues[x].append(characterList)
                except:
                    commanderByValues[x] = [characterList]


    for number in commanderByValues.keys():
        if number >= 2:
            for commander in commanderByValues[number]:
                commanderString = commander + " (" + str(number) + "): "
                for minions in commanders[commander]:
                    commanderString = commanderString + minions + ", "
                commanderString = commanderString[0:len(commanderString)-2:]
                commanderFileByNumbers.write(commanderString + "\n")

    commanders = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        commanderSearch = "-----"
        if minionsInfo[5] != "":
            commanderList = minionsInfo[5].split("|")
            for commander in commanderList:
                if commanderSearch == minions:
                    print("Reverse Commanders Match: " + commander)
                try:
                    commanders[minions].append(commander)
                except:
                    commanders[minions] = [commander]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    commandersPart2 = []
    for commander in commanders.keys():
        commandersPart2.append(commander)
    commanderFile = open("Statistics\\Minions\\reverse commanders.txt", "w",encoding='utf8')
    commanderFileByNumbers = open("Statistics\\Minions\\reverse commanders by numbers.txt", "w",encoding='utf8')

    commandersPart2.sort()
    for commander in commandersPart2:
        commanderString = commander + " (" + str(len(commanders[commander])) + "): "
        for wielden in commanders[commander]:
            commanderString = commanderString + wielden + ", "
        commanderString = commanderString[0:len(commanderString)-2:]
        commanderFile.write(commanderString + "\n")

    highNumber = -1
    for characterList in commanders.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    commanderByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in commanders.keys():
            if len(commanders[characterList]) == x:
                try:
                    commanderByValues[x].append(characterList)
                except:
                    commanderByValues[x] = [characterList]


    for number in commanderByValues.keys():
        if number >= 2:
            for commander in commanderByValues[number]:
                commanderString = commander + " (" + str(number) + "): "
                for minions in commanders[commander]:
                    commanderString = commanderString + minions + ", "
                commanderString = commanderString[0:len(commanderString)-2:]
                commanderFileByNumbers.write(commanderString + "\n")

    mediums = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        mediumSearch = "----"
        if minionsInfo[16] != "":
            mediumList = minionsInfo[16].split(",")
            for medium in mediumList:
                if mediumSearch == medium:
                    print("Mediums Match: " + minionsInfo[0] + " (" + minions + ")")
                try:
                    mediums[medium].append(minions)
                except:
                    mediums[medium] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    mediumsPart2 = []
    for medium in mediums.keys():
        mediumsPart2.append(medium)
    mediumFile = open("Statistics\\Minions\\mediums.txt", "w",encoding='utf8')
    mediumFileByNumbers = open("Statistics\\Minions\\mediums by numbers.txt", "w",encoding='utf8')

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
            for minions in mediums[medium]:
                mediumString = mediumString + minions + ", "
            mediumString = mediumString[0:len(mediumString)-2:]
            mediumFileByNumbers.write(mediumString + "\n")

    powerLevels = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        powerLevelSearch = "----"
        powerLevel = minionsInfo[13]
        if powerLevelSearch == powerLevel:
            print("Power Level Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            powerLevels[powerLevel].append(minions)
        except:
            powerLevels[powerLevel] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    powerLevelsPart2 = []
    for powerLevel in powerLevels.keys():
        powerLevelsPart2.append(powerLevel)
    powerLevelsFile = open("Statistics\\Minions\\power levels.txt", "w",encoding='utf8')
    powerLevelFileByNumbers = open("Statistics\\Minions\\power levels by numbers.txt", "w",encoding='utf8')

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
            for minions in powerLevels[powerLevel]:
                powerLevelString = powerLevelString + minions + ", "
            powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
            powerLevelFileByNumbers.write(powerLevelString + "\n")

    popularities = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        popularitySearch = "-----"
        popularity = minionsInfo[14]
        if popularitySearch == popularity:
            print("Popularity Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            popularities[popularity].append(minions)
        except:
            popularities[popularity] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    popularityPart2 = []
    for popularity in popularities.keys():
        popularityPart2.append(popularity)
    popularityFile = open("Statistics\\Minions\\popularity.txt", "w",encoding='utf8')
    popularityFileByNumbers = open("Statistics\\Minions\\popularity by numbers.txt", "w",encoding='utf8')

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
            for minions in popularities[popularity]:
                popularityString = popularityString + minions + ", "
            popularityString = popularityString[0:len(popularityString)-2:]
            popularityFileByNumbers.write(popularityString + "\n")


    colors = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        colorSearch = "-----"
        color = minionsInfo[18]
        if colorSearch == color:
            print("Color Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            colors[color].append(minions)
        except:
            colors[color] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    colorPart2 = []
    for color in colors.keys():
        colorPart2.append(color)
    colorFile = open("Statistics\\Minions\\color.txt", "w",encoding='utf8')
    colorFileByNumbers = open("Statistics\\Minions\\color by numbers.txt", "w",encoding='utf8')

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
                for minions in colors[color]:
                    colorString = colorString + minions + ", "
                colorString = colorString[0:len(colorString)-2:]
                colorFileByNumbers.write(colorString + "\n")
    
    
    types = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        typerSearch = "-----"
        typer = minionsInfo[9]
        if typerSearch == typer:
            print("Type Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            types[typer].append(minions)
        except:
            types[typer] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    typerPart2 = []
    for typer in types.keys():
        typerPart2.append(typer)
    typerFile = open("Statistics\\Minions\\type.txt", "w",encoding='utf8')
    typerFileByNumbers = open("Statistics\\Minions\\type by numbers.txt", "w",encoding='utf8')

    typerPart2.sort()
    for typer in typerPart2:
        typerString = typer + " (" + str(len(types[typer])) + "): "
        for colour in types[typer]:
            typerString = typerString + colour + ", "
        typerString = typerString[0:len(typerString)-2:]
        typerFile.write(typerString + "\n")

    highNumber = -1
    for characterList in types.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    typerByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in types.keys():
            if len(types[characterList]) == x:
                try:
                    typerByValues[x].append(characterList)
                except:
                    typerByValues[x] = [characterList]


    for number in typerByValues.keys():
        if number >= 2:
            for typer in typerByValues[number]:
                typerString = typer + " (" + str(number) + "): "
                for minions in types[typer]:
                    typerString = typerString + minions + ", "
                typerString = typerString[0:len(typerString)-2:]
                typerFileByNumbers.write(typerString + "\n")

    races = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        raceSearch = "-----"
        race = minionsInfo[10]
        if raceSearch == race:
            print("Race Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            races[race].append(minions)
        except:
            races[race] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    racePart2 = []
    for race in races.keys():
        racePart2.append(race)
    raceFile = open("Statistics\\Minions\\race.txt", "w",encoding='utf8')
    raceFileByNumbers = open("Statistics\\Minions\\race by numbers.txt", "w",encoding='utf8')

    racePart2.sort()
    for race in racePart2:
        raceString = race + " (" + str(len(races[race])) + "): "
        for colour in races[race]:
            raceString = raceString + colour + ", "
        raceString = raceString[0:len(raceString)-2:]
        raceFile.write(raceString + "\n")

    highNumber = -1
    for characterList in races.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    raceByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in races.keys():
            if len(races[characterList]) == x:
                try:
                    raceByValues[x].append(characterList)
                except:
                    raceByValues[x] = [characterList]


    for number in raceByValues.keys():
        if number >= 2:
            for race in raceByValues[number]:
                raceString = race + " (" + str(number) + "): "
                for minions in races[race]:
                    raceString = raceString + minions + ", "
                raceString = raceString[0:len(raceString)-2:]
                raceFileByNumbers.write(raceString + "\n")

    alignments = {}
    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")

        alignmentSearch = "-----"
        alignment = minionsInfo[18]
        if alignmentSearch == alignment:
            print("Alignments Match: " + minionsInfo[0] + " (" + minions + ")")
        try:
            alignments[alignment].append(minions)
        except:
            alignments[alignment] = [minions]
                    
                #else:
                    #print(minionsInfo[0] + " already expended " + characterTag)

    alignmentPart2 = []
    for alignment in alignments.keys():
        alignmentPart2.append(alignment)
    alignmentFile = open("Statistics\\Minions\\alignment.txt", "w",encoding='utf8')
    alignmentFileByNumbers = open("Statistics\\Minions\\alignment by numbers.txt", "w",encoding='utf8')

    alignmentPart2.sort()
    for alignment in alignmentPart2:
        alignmentString = alignment + " (" + str(len(alignments[alignment])) + "): "
        for colour in alignments[alignment]:
            alignmentString = alignmentString + colour + ", "
        alignmentString = alignmentString[0:len(alignmentString)-2:]
        alignmentFile.write(alignmentString + "\n")

    highNumber = -1
    for characterList in alignments.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    alignmentByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in alignments.keys():
            if len(alignments[characterList]) == x:
                try:
                    alignmentByValues[x].append(characterList)
                except:
                    alignmentByValues[x] = [characterList]


    for number in alignmentByValues.keys():
        if number >= 2:
            for alignment in alignmentByValues[number]:
                alignmentString = alignment + " (" + str(number) + "): "
                for minions in alignments[alignment]:
                    alignmentString = alignmentString + minions + ", "
                alignmentString = alignmentString[0:len(alignmentString)-2:]
                alignmentFileByNumbers.write(alignmentString + "\n")
    powersFile = open("Statistics\\Minions\\powers.txt", "w",encoding='utf8')
    powerDict = {}

    for minions in completedMinions:
        minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
        minionsInfo = minionsFile.read().split("\n")
        if minionsInfo[19] != "":
            minionPowers = minionsInfo[19].split(",")
            for powerSetFull in minionPowers:
                #print(entry[0:len(entry)-4:] + ": " + powerSetFull)
                powerSet = powerSetFull.split("|")
                minionPower = powerSet[0]
                minionPowerCategory = powerSet[1]
                minion = entry[0:len(entry)-4:] + " (Tier " + powerSet[2] + ")"
                try:
                    powerDict[minionPower][minionPowerCategory].append(minion)
                    powerDict[minionPower]["Total"].append(minion)
                except:
                    #print("Stage 1 failure (location: " + minion + ")")
                    try:
                        powerDict[minionPower][minionPowerCategory] = [minion]
                        powerDict[minionPower]["Total"].append(minion)
                    except:
                        #print("Stage 2 failure (location: " + minion + ")")
                        try:
                            powerDict[minionPower] = {minionPowerCategory: [minion],"Total":[minion]}
                        except:
                            print("It broke!")

    power2 = []
    for power in powerDict.keys():
        power2.append(power)
    power2.sort()

    powerString = ""
    for powerName in power2:
        powerSet = powerName + ":\n"
        powerSub2 = []
        for powerSubCat in powerDict[powerName].keys():
            powerSub2.append(powerSubCat)
        powerSub2.sort()
        for powerSubCategoryName in powerSub2:
            if powerSubCategoryName != "Total":
                powerSet = powerSet + "\t-" + powerSubCategoryName + " (" + str(len(powerDict[powerName][powerSubCategoryName])) + "/" + str(len(powerDict[powerName]["Total"])) + "): "
                for person in powerDict[powerName][powerSubCategoryName]:
                    powerSet = powerSet + person + ", "
                powerSet = powerSet[0:len(powerSet)-2:] + "\n"
        powerSet = powerSet + "\t-All " + " (" + str(len(powerDict[powerName]["Total"])) + "/" + str(len(completedMinions)) + "): "
        for person in powerDict[powerName]["Total"]:
            powerSet = powerSet + person + ", "
        powerSet = powerSet[0:len(powerSet)-2:] + "\n"
        powerString = powerString + "\n" + powerSet
        
    powersFile.write(powerString)