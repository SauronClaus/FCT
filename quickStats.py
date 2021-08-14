alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

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
            if len(characterInfo) == 24:
                completedCharacters.append(entry[0:len(entry)-4:])
            else:
                if len(characterInfo) == 5:
                    undoneCharacters.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 17 or len(characterInfo) == 22:
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

quickStatNum = str(len(completedCharacters)) + "/" + str(len(needToUpdateCharacters)) + "/" + str(len(undoneCharacters)) + "/" + str(len(weirdCharacters)) + " (Total: " + str(len(allCharacters)) + ")"

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
lastNameFile = open("Statistics\\Characters\\lastNames.txt", "w",encoding='utf8')\

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
    if len(years[str(year)]) >= 2:
        yearString = str(year) + " (" + str(len(years[str(year)])) + "): "
        for character in years[str(year)]:
            yearString = yearString + character + ", "
        yearString = yearString[0:len(yearString)-2:]
        yearFile.write(yearString + "\n")
for decade in decadesPart2:
    if len(decades[str(decade)]) >= 2:
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
        if len(types[typeName]) >= 2:
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
            races[characterRace]+=1
        except:
            races[characterRace] = 1

racesPart2 = []
for race in races.keys():
    racesPart2.append(race)
raceFile = open("Statistics\\Characters\\races.txt", "w",encoding='utf8')
racesPart2.sort()
for race in racesPart2:
    raceFile.write(race + ": " + str(races[race]) + "\n")

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
            alignments[characterAlignment]+=1
        except:
            alignments[characterAlignment] = 1

alignmentsPart2 = []
for alignment in alignments.keys():
    alignmentsPart2.append(alignment)
alignmentFile = open("Statistics\\Characters\\alignments.txt", "w",encoding='utf8')
alignmentsPart2.sort()
for alignment in alignmentsPart2:
    alignmentFile.write(alignment + ": " + str(alignments[alignment]) + "\n")

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
            roles[characterRole]+=1
        except:
            roles[characterRole] = 1

rolesPart2 = []
for role in roles.keys():
    rolesPart2.append(role)
roleFile = open("Statistics\\Characters\\roles.txt", "w",encoding='utf8')
rolesPart2.sort()
for role in rolesPart2:
    roleFile.write(role + ": " + str(roles[role]) + "\n")

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
            genders[characterGender]+=1
        except:
            genders[characterGender] = 1

gendersPart2 = []
for gender in genders.keys():
    gendersPart2.append(gender)
genderFile = open("Statistics\\Characters\\genders.txt", "w",encoding='utf8')
gendersPart2.sort()
for gender in gendersPart2:
    genderFile.write(gender + ": " + str(genders[gender]) + "\n")

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
            powerLevels[characterPowerLevel]+=1
        except:
            powerLevels[characterPowerLevel] = 1

powerLevelsPart2 = []
for powerLevel in powerLevels.keys():
    powerLevelsPart2.append(powerLevel)
powerLevelsFile = open("Statistics\\Characters\\power levels.txt", "w",encoding='utf8')
powerLevelsPart2.sort()
for powerLevel in powerLevelsPart2:
    powerLevelsFile.write(powerLevel + ": " + str(powerLevels[powerLevel]) + "\n")

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
            popularities[characterPopularity]+=1
        except:
            popularities[characterPopularity] = 1

popularitiesPart2 = []
for popularity in popularities.keys():
    popularitiesPart2.append(popularity)
popularitiesFile = open("Statistics\\Characters\\popularities.txt", "w",encoding='utf8')
popularitiesPart2.sort()
for popularity in popularitiesPart2:
    popularitiesFile.write(popularity + ": " + str(popularities[popularity]) + "\n")

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
                mediums[characterMedium]+=1
            except:
                mediums[characterMedium] = 1

mediumsPart2 = []
for medium in mediums.keys():
    mediumsPart2.append(medium)
mediumsFile = open("Statistics\\Characters\\mediums.txt", "w",encoding='utf8')
mediumsPart2.sort()
for medium in mediumsPart2:
    mediumsFile.write(medium + ": " + str(mediums[medium]) + "\n")

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
            colors[characterColor]+=1
        except:
            colors[characterColor] = 1

colorsPart2 = []
for color in colors.keys():
    colorsPart2.append(color)
colorFile = open("Statistics\\Characters\\colors.txt", "w",encoding='utf8')
colorsPart2.sort()
for color in colorsPart2:
    colorFile.write(color + ": " + str(colors[color]) + "\n")

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
                groups[characterGroup]+=1
            except:
                groups[characterGroup] = 1

groupsPart2 = []
for group in groups.keys():
    groupsPart2.append(group)
groupFile = open("Statistics\\Characters\\groups.txt", "w",encoding='utf8')
groupsPart2.sort()
for group in groupsPart2:
    groupFile.write(group + ": " + str(groups[group]) + "\n")


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
            characterTag = characterTagFull.split("|")[0]
            if tagSearch == characterTag:
                print("Tag Match: " + characterInfo[0] + " (" + character + ")")
            if not (characterTag in tagsExpended):
                try:
                    tags[characterTag]+=1
                except:
                    tags[characterTag] = 1
                tagsExpended.append(characterTag)
            #else:
                #print(characterInfo[0] + " already expended " + characterTag)

tagsPart2 = []
for tag in tags.keys():
    tagsPart2.append(tag)
tagFile = open("Statistics\\Characters\\tags.txt", "w",encoding='utf8')
tagsPart2.sort()
for tag in tagsPart2:
    tagFile.write(tag + ": " + str(tags[tag]) + "\n")

highestNum = 0
for typeIt in typesPart2:
    if len(types[typeIt]) > highestNum and typeIt != "Superhero" and typeIt != "Fighter":
        highestNum = len(types[typeIt])



weirdFile = open("Statistics\\Completetion Rankings\\People\\weirdCharacters.txt", "w", encoding='utf8')
updateFile = open("Statistics\\Completetion Rankings\\People\\needToUpdateCharacters.txt", "w", encoding='utf8')
incompleteFile = open("Statistics\\Completetion Rankings\\People\\incompleteCharacters.txt", "w", encoding='utf8')
completeFile = open("Statistics\\Completetion Rankings\\People\\completedCharacters.txt", "w", encoding='utf8')

completedCharacters.sort()
undoneCharacters.sort()
needToUpdateCharacters.sort()
weirdCharacters.sort()

for character in completedCharacters:
    completeFile.write(character + "\n")

for character in undoneCharacters:
    incompleteFile.write(character + "\n")
for character in needToUpdateCharacters:
    updateFile.write(character + "\n")
for character in weirdCharacters:
    weirdFile.write(character + "\n")

weirdFile.close()
updateFile.close()
incompleteFile.close()
completeFile.close()


weirdFile = open("Statistics\\Completetion Rankings\\Franchises\\weirdFranchises.txt", "w", encoding='utf8')
updateFile = open("Statistics\\Completetion Rankings\\Franchises\\needToUpdateFranchises.txt", "w", encoding='utf8')
incompleteFile = open("Statistics\\Completetion Rankings\\Franchises\\incompleteFranchises.txt", "w", encoding='utf8')
completeFile = open("Statistics\\Completetion Rankings\\Franchises\\completedFranchises.txt", "w", encoding='utf8')


completedFranchises = []
undoneFranchises = []
needToUpdateFranchises = []
weirdFranchises = []

for letter in alphabet:
    basepath = 'Franchises/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
            franchiseInfo = franchiseFile.read().split("\n")
            if len(franchiseInfo) == 17:
                completedFranchises.append(entry[0:len(entry)-4:])
            else:
                if len(franchiseInfo) == 7:
                    needToUpdateFranchises.append(entry[0:len(entry)-4:])
                else:
                    if len(franchiseInfo) == 2:
                        undoneFranchises.append(entry[0:len(entry)-4:])
                    else:
                        weirdFranchises.append(entry[0:len(entry)-4:])

completedFranchises.sort()
undoneFranchises.sort()
needToUpdateFranchises.sort()
weirdFranchises.sort()

for franchise in weirdFranchises:
    weirdFile.write(franchise + "\n")
for franchise in needToUpdateFranchises:
    updateFile.write(franchise + "\n")
for franchise in undoneFranchises:
    incompleteFile.write(franchise + "\n")
for franchise in completedFranchises:
    completeFile.write(franchise + "\n")

weirdFile.close()
updateFile.close()
incompleteFile.close()
completeFile.close()

weirdFile = open("Statistics\\Completetion Rankings\\Artifacts\\weirdArtifacts.txt", "w", encoding='utf8')
updateFile = open("Statistics\\Completetion Rankings\\Artifacts\\needToUpdateArtifacts.txt", "w", encoding='utf8')
incompleteFile = open("Statistics\\Completetion Rankings\\Artifacts\\incompleteArtifacts.txt", "w", encoding='utf8')
completeFile = open("Statistics\\Completetion Rankings\\Artifacts\\completedArtifacts.txt", "w", encoding='utf8')


completedArtifacts = []
undoneArtifacts = []
needToUpdateArtifacts = []
weirdArtifacts = []

basepath = "Artifacts"
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        ArtifactsFile = open(basepath + "/" + entry, "r", encoding='utf8')
        ArtifactsInfo = ArtifactsFile.read().split("\n")
        if entry != "readMe.txt":
            if len(ArtifactsInfo) == 14:
                completedArtifacts.append(entry[0:len(entry)-4:])
            else:
                if len(ArtifactsInfo) == 0:
                    needToUpdateArtifacts.append(entry[0:len(entry)-4:])
                else:
                    if len(ArtifactsInfo) == 9:
                        undoneArtifacts.append(entry[0:len(entry)-4:])
                    else:
                        weirdArtifacts.append(entry[0:len(entry)-4:])

completedArtifacts.sort()
undoneArtifacts.sort()
needToUpdateArtifacts.sort()
weirdArtifacts.sort()

for artifact in weirdArtifacts:
    weirdFile.write(artifact + "\n")
for artifact in needToUpdateArtifacts:
    updateFile.write(artifact + "\n")
for artifact in undoneArtifacts:
    incompleteFile.write(artifact + "\n")
for artifact in completedArtifacts:
    completeFile.write(artifact + "\n")

weirdFile.close()
updateFile.close()
incompleteFile.close()
completeFile.close()

print("High Number: " + str(highestNum))
print("Completed!")

