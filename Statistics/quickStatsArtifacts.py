# This program fills out all of the quick stat files inside the folder Statistics\\Artifacts

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

def quickStatsArtifacts():
    completedArtifacts = []
    undoneArtifacts = []
    needToUpdateArtifacts = []
    weirdArtifacts = []
    allArtifacts = []

    basepath = "Artifacts"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            ArtifactsFile = open(basepath + "/" + entry, "r", encoding='utf8')
            ArtifactsInfo = ArtifactsFile.read().split("\n")
            if entry != "readMe.txt":
                if len(ArtifactsInfo) == 16:
                    completedArtifacts.append(entry[0:len(entry)-4:])
                else:
                    if len(ArtifactsInfo) == 0:
                        needToUpdateArtifacts.append(entry[0:len(entry)-4:])
                    else:
                        if len(ArtifactsInfo) == 9:
                            undoneArtifacts.append(entry[0:len(entry)-4:])
                        else:
                            weirdArtifacts.append(entry[0:len(entry)-4:])
                allArtifacts.append(entry[0:len(entry)-4:])

    completedArtifacts.sort()
    undoneArtifacts.sort()
    needToUpdateArtifacts.sort()
    weirdArtifacts.sort()
    allArtifacts.sort()

    statsFile = open("Statistics\\Artifacts\\stats.txt", "w",encoding='utf8')
    quickStatNum = str(len(completedArtifacts)) + " (completed)/" + str(len(needToUpdateArtifacts)) + " (need to update)/" + str(len(undoneArtifacts)) + " (incompleted)/" + str(len(weirdArtifacts)) + " (weird)/Total: " + str(len(allArtifacts))
    statsFile.write(quickStatNum)

    artifactBrands = {}
    artifactBrandsFile = open("Statistics\\Artifacts\\artifactBrands.txt", "w",encoding='utf8')

    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")
        searchFranchise = ""

        artifactBrand = artifactInfo[1]
        artifactFranchise = artifactInfo[5]
        if artifactFranchise == searchFranchise:
            print("-" + artifactInfo[0] + " (" + artifact + ") is in " + artifactBrand + ": " + artifactFranchise + " (Franchise)")
        try:
            artifactBrands[artifactBrand][artifactFranchise].append(artifact)
            artifactBrands[artifactBrand]["Total"].append(artifact)
        except:
            #print("Stage 1 failure (location: " + artifact + ")")
            try:
                artifactBrands[artifactBrand][artifactFranchise] = [artifact]
                artifactBrands[artifactBrand]["Total"].append(artifact)
            except:
                #print("Stage 2 failure (location: " + artifact + ")")
                try:
                    artifactBrands[artifactBrand] = {artifactFranchise: [artifact],"Total":[artifact]}
                except:
                    print("It broke!")

    artifactBrandList = []
    for artifactBrand in artifactBrands.keys():
        artifactBrandList.append(artifactBrand)
    artifactBrandList.sort()


    brandString = ""
    for brandName in artifactBrandList:
        brandSet = brandName + " (" + str(len(artifactBrands[brandName]["Total"])) + "/" + str(len(completedArtifacts)) + "):\n"
        for franchiseName in artifactBrands[brandName].keys():
            if franchiseName != "Total":
                brandSet = brandSet + "\t-" + franchiseName + " (" + str(len(artifactBrands[brandName][franchiseName])) + "/" + str(len(artifactBrands[brandName]["Total"])) + "): "
                for person in artifactBrands[brandName][franchiseName]:
                    brandSet = brandSet + person + ", "
                brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandSet = brandSet + "\t-All " + " (" + str(len(artifactBrands[brandName]["Total"])) + "/" + str(len(completedArtifacts)) + "): "
        for person in artifactBrands[brandName]["Total"]:
            brandSet = brandSet + person + ", "
        brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandString = brandString + "\n" + brandSet
        
    artifactBrandsFile.write(brandString)

    artifactTypes = {}
    artifactTypesFile = open("Statistics\\Artifacts\\artifactTypes.txt", "w",encoding='utf8')

    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")
        searchFranchise = ""

        artifactDouble = artifactInfo[9].split("|")
        artifactCategory = artifactDouble[0]
        artifactSubcategory = artifactDouble[1]
        if artifactSubcategory == searchFranchise:
            print("-" + artifactInfo[0] + " (" + artifact + ") is in " + artifactCategory + ": " + artifactSubcategory + " (Franchise)")
        try:
            artifactTypes[artifactCategory][artifactSubcategory].append(artifact)
            artifactTypes[artifactCategory]["Total"].append(artifact)
        except:
            #print("Stage 1 failure (location: " + artifact + ")")
            try:
                artifactTypes[artifactCategory][artifactSubcategory] = [artifact]
                artifactTypes[artifactCategory]["Total"].append(artifact)
            except:
                #print("Stage 2 failure (location: " + artifact + ")")
                try:
                    artifactTypes[artifactCategory] = {artifactSubcategory: [artifact],"Total":[artifact]}
                except:
                    print("It broke!")

    artifactTypeList = []
    for artifactType in artifactTypes.keys():
        artifactTypeList.append(artifactType)
    artifactTypeList.sort()
    brandString = ""
    for brandName in artifactTypeList:
        brandSet = brandName + ":\n"
        for franchiseName in artifactTypes[brandName].keys():
            if franchiseName != "Total":
                brandSet = brandSet + "\t-" + franchiseName + " (" + str(len(artifactTypes[brandName][franchiseName])) + "/" + str(len(artifactTypes[brandName]["Total"])) + "): "
                for person in artifactTypes[brandName][franchiseName]:
                    brandSet = brandSet + person + ", "
                brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandSet = brandSet + "\t-All " + " (" + str(len(artifactTypes[brandName]["Total"])) + "/" + str(len(completedArtifacts)) + "): "
        for person in artifactTypes[brandName]["Total"]:
            brandSet = brandSet + person + ", "
        brandSet = brandSet[0:len(brandSet)-2:] + "\n"
        brandString = brandString + "\n" + brandSet
        
    artifactTypesFile.write(brandString)

    tags = {}
    for artifact in completedArtifacts:
        tagsExpended = []
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        tagSearch = "Tara Strong"
        if artifactInfo[7] != "":
            characterTagList = artifactInfo[7].split(",")
            for characterTagFull in characterTagList:
                characterTag = characterTagFull.split("|")
                if tagSearch == characterTag[0]:
                    print("Tag Match: " + artifactInfo[0] + " (" + artifact + ")")
                if not (characterTag[0] in tagsExpended):
                    if len(characterTag) >= 2:
                        try:
                            tags[characterTag[0]].append(artifact + " (" + characterTag[1] + ")")
                        except:
                            tags[characterTag[0]] = [artifact + " (" + characterTag[1] + ")"]
                    else:
                        try:
                            tags[characterTag[0]].append(artifact)
                        except:
                            tags[characterTag[0]] = [artifact]
                    tagsExpended.append(characterTag[0])
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    tagsPart2 = []
    for tag in tags.keys():
        tagsPart2.append(tag)
    tagFile = open("Statistics\\Artifacts\\tags.txt", "w",encoding='utf8')
    tagFileByNumbers = open("Statistics\\Artifacts\\tags by numbers.txt", "w",encoding='utf8')

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
            for artifact in tags[tag]:
                tagString = tagString + artifact + ", "
            tagString = tagString[0:len(tagString)-2:]
            tagFileByNumbers.write(tagString + "\n")

    wielders = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        wielderSearch = "---"
        if artifactInfo[6] != "":
            wielderList = artifactInfo[6].split("|")
            for wielder in wielderList:
                if wielderSearch == wielder:
                    print("Wielders Match: " + artifactInfo[0] + " (" + artifact + ")")
                try:
                    wielders[wielder].append(artifact)
                except:
                    wielders[wielder] = [artifact]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    wieldersPart2 = []
    for wielder in wielders.keys():
        wieldersPart2.append(wielder)
    wielderFile = open("Statistics\\Artifacts\\wielders.txt", "w",encoding='utf8')
    wielderFileByNumbers = open("Statistics\\Artifacts\\wielders by numbers.txt", "w",encoding='utf8')

    wieldersPart2.sort()
    for wielder in wieldersPart2:
        wielderString = wielder + " (" + str(len(wielders[wielder])) + "): "
        for wielden in wielders[wielder]:
            wielderString = wielderString + wielden + ", "
        wielderString = wielderString[0:len(wielderString)-2:]
        wielderFile.write(wielderString + "\n")

    highNumber = -1
    for characterList in wielders.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    wielderByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in wielders.keys():
            if len(wielders[characterList]) == x:
                try:
                    wielderByValues[x].append(characterList)
                except:
                    wielderByValues[x] = [characterList]


    for number in wielderByValues.keys():
        if number >= 2:
            for wielder in wielderByValues[number]:
                wielderString = wielder + " (" + str(number) + "): "
                for artifact in wielders[wielder]:
                    wielderString = wielderString + artifact + ", "
                wielderString = wielderString[0:len(wielderString)-2:]
                wielderFileByNumbers.write(wielderString + "\n")

    wielders = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        wielderSearch = "-----"
        if artifactInfo[6] != "":
            wielderList = artifactInfo[6].split("|")
            for wielder in wielderList:
                if wielderSearch == artifact:
                    print("Reverse Wielders Match: " + wielder)
                try:
                    wielders[artifact].append(wielder)
                except:
                    wielders[artifact] = [wielder]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    wieldersPart2 = []
    for wielder in wielders.keys():
        wieldersPart2.append(wielder)
    wielderFile = open("Statistics\\Artifacts\\reverse wielders.txt", "w",encoding='utf8')
    wielderFileByNumbers = open("Statistics\\Artifacts\\reverse wielders by numbers.txt", "w",encoding='utf8')

    wieldersPart2.sort()
    for wielder in wieldersPart2:
        wielderString = wielder + " (" + str(len(wielders[wielder])) + "): "
        for wielden in wielders[wielder]:
            wielderString = wielderString + wielden + ", "
        wielderString = wielderString[0:len(wielderString)-2:]
        wielderFile.write(wielderString + "\n")

    highNumber = -1
    for characterList in wielders.values():
        if len(characterList) > highNumber:
            highNumber = len(characterList)

    wielderByValues = {}
    for x in reversed(range(highNumber + 1)):
        for characterList in wielders.keys():
            if len(wielders[characterList]) == x:
                try:
                    wielderByValues[x].append(characterList)
                except:
                    wielderByValues[x] = [characterList]


    for number in wielderByValues.keys():
        if number >= 2:
            for wielder in wielderByValues[number]:
                wielderString = wielder + " (" + str(number) + "): "
                for artifact in wielders[wielder]:
                    wielderString = wielderString + artifact + ", "
                wielderString = wielderString[0:len(wielderString)-2:]
                wielderFileByNumbers.write(wielderString + "\n")

    mediums = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        mediumSearch = "----"
        if artifactInfo[8] != "":
            mediumList = artifactInfo[8].split(",")
            for medium in mediumList:
                if mediumSearch == medium:
                    print("Mediums Match: " + artifactInfo[0] + " (" + artifact + ")")
                try:
                    mediums[medium].append(artifact)
                except:
                    mediums[medium] = [artifact]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    mediumsPart2 = []
    for medium in mediums.keys():
        mediumsPart2.append(medium)
    mediumFile = open("Statistics\\Artifacts\\mediums.txt", "w",encoding='utf8')
    mediumFileByNumbers = open("Statistics\\Artifacts\\mediums by numbers.txt", "w",encoding='utf8')

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
            for artifact in mediums[medium]:
                mediumString = mediumString + artifact + ", "
            mediumString = mediumString[0:len(mediumString)-2:]
            mediumFileByNumbers.write(mediumString + "\n")

    powerLevels = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        powerLevelSearch = "----"
        powerLevel = artifactInfo[11]
        if powerLevelSearch == powerLevel:
            print("Power Level Match: " + artifactInfo[0] + " (" + artifact + ")")
        try:
            powerLevels[powerLevel].append(artifact)
        except:
            powerLevels[powerLevel] = [artifact]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    powerLevelsPart2 = []
    for powerLevel in powerLevels.keys():
        powerLevelsPart2.append(powerLevel)
    powerLevelsFile = open("Statistics\\Artifacts\\power levels.txt", "w",encoding='utf8')
    powerLevelFileByNumbers = open("Statistics\\Artifacts\\power levels by numbers.txt", "w",encoding='utf8')

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
            for artifact in powerLevels[powerLevel]:
                powerLevelString = powerLevelString + artifact + ", "
            powerLevelString = powerLevelString[0:len(powerLevelString)-2:]
            powerLevelFileByNumbers.write(powerLevelString + "\n")

    popularities = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        popularitySearch = "-----"
        popularity = artifactInfo[12]
        if popularitySearch == popularity:
            print("Popularity Match: " + artifactInfo[0] + " (" + artifact + ")")
        try:
            popularities[popularity].append(artifact)
        except:
            popularities[popularity] = [artifact]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    popularityPart2 = []
    for popularity in popularities.keys():
        popularityPart2.append(popularity)
    popularityFile = open("Statistics\\Artifacts\\popularity.txt", "w",encoding='utf8')
    popularityFileByNumbers = open("Statistics\\Artifacts\\popularity by numbers.txt", "w",encoding='utf8')

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
            for artifact in popularities[popularity]:
                popularityString = popularityString + artifact + ", "
            popularityString = popularityString[0:len(popularityString)-2:]
            popularityFileByNumbers.write(popularityString + "\n")


    colors = {}
    for artifact in completedArtifacts:
        artifactFile = open("Artifacts\\" + artifact + ".txt", "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")

        colorSearch = "-----"
        color = artifactInfo[13]
        if colorSearch == color:
            print("Color Match: " + artifactInfo[0] + " (" + artifact + ")")
        try:
            colors[color].append(artifact)
        except:
            colors[color] = [artifact]
                    
                #else:
                    #print(artifactInfo[0] + " already expended " + characterTag)

    colorPart2 = []
    for color in colors.keys():
        colorPart2.append(color)
    colorFile = open("Statistics\\Artifacts\\color.txt", "w",encoding='utf8')
    colorFileByNumbers = open("Statistics\\Artifacts\\color by numbers.txt", "w",encoding='utf8')

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
                for artifact in colors[color]:
                    colorString = colorString + artifact + ", "
                colorString = colorString[0:len(colorString)-2:]
                colorFileByNumbers.write(colorString + "\n")



    print("Completed Artifact Updates!")