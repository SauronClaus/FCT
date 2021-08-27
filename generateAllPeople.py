# Generates the people needed. Follows through from generation.py

import random
import os
from all import allFranchises
from all import allGroups
from all import allPeople
from all import allMinions

from generateAdjective import generateAdjective

from generateOdds import chooseCharacter


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

powerLevelsDict = {"Baseline": 0, "Modified Human": 1, "City": 2, "Country": 3, "World": 4, "Cosmic": 5, "Interuniversal": 6, "Omnipotent": 7}
additionalPowerLevels = {4: "Tier 1", 3: "Tier 2", 2: "Tier 3", 1: "Tier 4"}

def genAllPeople(guildID, peopleReplacementOrigs, franchiseInfo, otherAddedCharacters, antagonists):
    print("People Replace: " + str(peopleReplacementOrigs))
    maxPowerLevel = -1
    for powerLevel in powerLevelsDict.values():
        maxPowerLevel = powerLevel
    print("Max Power Level: " + str(maxPowerLevel) + "\n")
    franchiseGroups = allGroups() #a dict of string/list pairs; the string is the group name, the list is the people in the group.
    people = allPeople()
    
    charactersReplacement = {}
    for person in peopleReplacementOrigs:
        charactersReplacement[person] = "Incomplete"

    subbedPeople = [] # List of people being subbed into the franchise. 

    groupReplacementRNG = random.randint(1,4)
    validGroups = {} # This dict's key is the group name (from groupsCanReplace) and the value is a list of the possible replacement 
    # groups. (the ones with the same number of people in them as the original)
    groupsCanReplace = [] # List of groups to replace (strings)
    endValidGroups = [] # End valid groups is, in the end, a duplicate of groupsCanReplace that we use to iterate through groupsCanReplace 
    # and remove the invalid groups.

    reasonSubbing = {}
    peopleAdjectives = {}

    for person in peopleReplacementOrigs:
        if person != "":
            groupsPerson = people[person][18].split(",")
            for group in groupsPerson:
                if not(group in groupsCanReplace) and group != "":
                    groupsCanReplace.append(group)
                    endValidGroups.append(group)
    # This makes groupsCanReplace (and, by extension, endValidGroups) a full list of all the groups in all the people in the franchise
    # file. 

    if groupReplacementRNG == 4 and len(groupsCanReplace) > 0:
        print("Replacing via groups.")
        groupPowerLevels = {}
        for group in endValidGroups:
            for personGroupMember in franchiseGroups[group]:
                if not(personGroupMember in peopleReplacementOrigs) and group in groupsCanReplace:
                    print("Removed " + group + " because of the exclusion of " + personGroupMember)
                    groupsCanReplace.remove(group)
                if len(franchiseGroups[group]) <= 1:
                    print("Removed " + group + " because of the membership of only " + personGroupMember)
                    groupsCanReplace.remove(group)
        # Now, this bit removes all the groups that aren't valid, either because the group only has one person in it or because somebody in
        # the group isn't in the current replace Franchise. 
        print("\n")
        testString = ""
        for group in groupsCanReplace:
            testString = testString + group + ", "
        testString = testString[0:len(testString)-2:]
        print("For " + franchiseInfo[0] + ", " + str(len(groupsCanReplace)) + " groups were found in total. (" + testString + ")")
        
        # This is just a little method that prints out the groups at this stage in the process. 
        for group in groupsCanReplace:
            groupPowerLevel = 0
            for person in franchiseGroups[group]:
                personalPowerLevel = powerLevelsDict[people[person][16]]
                print("Adding " + person + " to the power level (" + people[person][16] + "/" + str(personalPowerLevel) + ")")
                groupPowerLevel+=personalPowerLevel
            print("Final " + group + " Power Level: " + str(groupPowerLevel) + "\n")
            groupPowerLevels[group] = groupPowerLevel
        
        for validGroup in groupsCanReplace:
            groups = {} # A dict of group's- the key is the group name, the value is the number of people in that group. 
            for character in people.keys():
                characterInfo = people[character]
                if characterInfo[1] != franchiseInfo[11]:
                    for group in characterInfo[18].split(","):
                        if not(group in groupsCanReplace):
                            try:
                                groups[group] += 1
                            except:
                                groups[group] = 1
            # In the end, this just makes a massive dict of every group as long as the group isn't in the replacement franchise.
            for group in groups.keys():
                if group != "":
                    groupPowerLevel = 0
                    for person in franchiseGroups[group]:
                        personalPowerLevel = powerLevelsDict[people[person][16]]
                        groupPowerLevel+=personalPowerLevel
                    if groups[group] == len(franchiseGroups[validGroup]) and groupPowerLevel in range(groupPowerLevels[validGroup]-len(franchiseGroups[validGroup]),groupPowerLevels[validGroup]+len(franchiseGroups[validGroup])):
                        print(group + "'s power level of " + str(groupPowerLevel) + " was within range of " + str(groupPowerLevels[validGroup]-len(franchiseGroups[validGroup])) + " and " + str(groupPowerLevels[validGroup]+len(franchiseGroups[validGroup])) + "!")
                        try:
                            validGroups[validGroup].append(group)
                        except:
                            validGroups[validGroup] = [group]
            # This one adds the groups in the groups dict to validGroups if they have the right number of people in them. 
        
        invalidGroups = [] # a list of the invalid groups? Unclear on how things are added to it.
        for replaceGroup in validGroups.keys():
            if len(validGroups[replaceGroup]) == 0:
                print(replaceGroup + " doesn't have any valid matches!")
                invalidGroups.append(replaceGroup)
        # Essentially if a group in validGroups has no shared numbers, then it says that it doesn't work and adds that group to 
        # invalidGroups.
        for inval in invalidGroups:
            del validGroups[inval]
        # Each invalidGroup is removed from validGroups.
        for replaceGroup in validGroups.keys():
            if len(validGroups[replaceGroup]) <= 5:
                testString = ""
                for group in validGroups[replaceGroup]:
                    testString = testString + group + ", "
                testString = testString[0:len(testString)-2:]
                print(replaceGroup + ": " + testString + " (" + str(len(franchiseGroups[replaceGroup])) + " members in group)")
            else:
                print(replaceGroup + ": " + str(len(validGroups[replaceGroup])) + " (" + str(len(franchiseGroups[replaceGroup])) + " members in group)")
            testString = ""
            for group in franchiseGroups[replaceGroup]:
                testString = testString + group + ", "
            testString = testString[0:len(testString)-2:]
            print(replaceGroup + ": " + testString)
        # Now we've hit this point, so for every valid group it prints out. If there's 5 groups or fewer, it prints all of them out, but 
        # at more than 5 it prints out just the number of groups.
                
        reverseFranchiseGroups = {}
        for group in franchiseGroups.keys():
            for person in franchiseGroups[group]:
                if person in peopleReplacementOrigs and group in validGroups.keys():
                    try:
                        reverseFranchiseGroups[person].append(group)
                    except:
                        reverseFranchiseGroups[person] = [group]
        
        franchiseGroupEnd = {} # Dict. Key is person name, value is franchise name.
        reverseFranchiseGroupsKeys = []
        for person in reverseFranchiseGroups.keys():
            reverseFranchiseGroupsKeys.append(person)
        print("\n")

        random.shuffle(reverseFranchiseGroupsKeys)

        testString = ""
        for person in reverseFranchiseGroupsKeys:
            testString = testString + person + ", "
        testString = "Shuffled People: " + testString[0:len(testString)-2:]
        print(testString)

        chosenGroups = {} # A dict; key is the name of the franchise that's being subbed in, value is the 
        # franchise that subs it. 
        newlyInvalidGroups = []

        for person in reverseFranchiseGroupsKeys:
            if len(reverseFranchiseGroups[person]) == 1:
                group = reverseFranchiseGroups[person][0]
                if not(group in newlyInvalidGroups):
                    print(person + ": " + group + " (default remaining option)")
                    if not(group in chosenGroups.keys()):
                            #chosenGroups.append(group)
                            RNG = random.randint(0,len(validGroups[group])-1)
                            chosenGroups[group] = validGroups[group][RNG]

                    franchiseGroupEnd[person] = chosenGroups[group]
                    for groupRemove in reverseFranchiseGroups[person]:
                        if groupRemove != group:
                            newlyInvalidGroups.append(groupRemove)
                            print("Removed " + groupRemove + " from " + person + ". (default group); remaing groups " + str(reverseFranchiseGroups[person]))
                    for personGroupsRemove in franchiseGroups[group]:
                            for personsGroup in reverseFranchiseGroups[personGroupsRemove]:
                                if personsGroup != group:
                                    newlyInvalidGroups.append(personsGroup)
                                    print("Removed " + personsGroup + " from " + person + ". (default option new loop)")
                else:
                    print("-----------Removed " + person + " (only remaining group, " + group + " was invalid.)")      
            if len(reverseFranchiseGroups[person]) > 1:
                choseGroup = False
                for group in reverseFranchiseGroups[person]:
                    if group in chosenGroups.keys():
                        print(group + " was already chosen; removing " + person + " from play. (" + str(len(chosenGroups)) + " chosen groups)")
                        print(person + ": " + group + " (already chosen group)")
                        franchiseGroupEnd[person] = chosenGroups[group]

                        for groupRemove in reverseFranchiseGroups[person]:
                            if groupRemove != group:
                                    newlyInvalidGroups.append(groupRemove)
                                    print("Removed " + groupRemove + " from " + person + ". (already chosen group); remaing groups " + str(reverseFranchiseGroups[person]))
                            else:
                                for personRemoval in reverseFranchiseGroups.keys():
                                    for finishedPerson in franchiseGroups[group]:
                                        if personRemoval == finishedPerson:
                                            print(finishedPerson + ": " + group + " (already chosen group's extended cut)")
                                            franchiseGroupEnd[person] = chosenGroups[group]
                        for personGroupsRemove in franchiseGroups[group]:
                            for personsGroup in reverseFranchiseGroups[personGroupsRemove]:
                                if personsGroup != group:
                                    newlyInvalidGroups.append(personsGroup)
                                    print("Removed " + personsGroup + " from " + person + ". (new loop already chosen)")
                                    
                        choseGroup = True
                if choseGroup == False:
                    print("Found that " + person + " has " + str(len(reverseFranchiseGroups[person])) + " groups.")
                    RNG = random.randint(0,len(reverseFranchiseGroups[person])-1)
                    group = reverseFranchiseGroups[person][RNG]
                    print(person + ": " + group + " (new group)")
                    if not(group in chosenGroups.keys()):
                        #chosenGroups.append(group)
                        RNG = random.randint(0,len(validGroups[group])-1)
                        chosenGroups[group] = validGroups[group][RNG]
                        
                    franchiseGroupEnd[person] = chosenGroups[group]

                    for groupRemove in reverseFranchiseGroups[person]:
                        if groupRemove != group:
                            newlyInvalidGroups.append(groupRemove)
                            print("Removed " + groupRemove + " from " + person + ". (new group); remaining groups " + str(reverseFranchiseGroups[person]))
                            #print("Removed " + groupRemove + " from " + personRemoval)
                        else:
                            for personRemoval in reverseFranchiseGroups.keys():
                                for finishedPerson in franchiseGroups[group]:
                                    if personRemoval == finishedPerson:
                                        print(finishedPerson + ": " + group + " (new group's extended cut)")
                                        franchiseGroupEnd[person] = chosenGroups[group]
                    for personGroupsRemove in franchiseGroups[group]:
                            for personsGroup in reverseFranchiseGroups[personGroupsRemove]:
                                if personsGroup != group:
                                    newlyInvalidGroups.append(personsGroup)
                                    print("Removed " + personsGroup + " from " + person + ". (new loop new group)")
            for invalidGroup in newlyInvalidGroups:
                #print("---> Begin Invalid Loop; Invalid Group: " + str(newlyInvalidGroups))
                for newlyInvalidPerson in franchiseGroups[invalidGroup]:
                    if newlyInvalidPerson in reverseFranchiseGroups.keys():
                        if invalidGroup in reverseFranchiseGroups[newlyInvalidPerson]:
                            reverseFranchiseGroups[newlyInvalidPerson].remove(invalidGroup)
                            print("Removed " + invalidGroup + " from " + newlyInvalidPerson + " (invalid loop)")
            #print("---> Loop finish")
        # Each invalidGroup is removed from validGroups.
        print("\n")
        for origGroup in chosenGroups.keys():
            print("Substituted " + chosenGroups[origGroup] + " for " + origGroup)
        print("\n")

        for validPeople in franchiseGroupEnd.keys():
            #print("Finals: " + validPeople + " in " + franchiseGroupEnd[validPeople])
            subFranchise = franchiseGroups[franchiseGroupEnd[validPeople]]
            exitCondition = ":("
            chosenCharacter = ""
            while exitCondition == ":(":
                RNG = random.randint(0,len(subFranchise)-1)
                chosenCharacter = subFranchise[RNG]
                #print("Generated " + chosenCharacter + " for " + validPeople)
                if not(chosenCharacter in subbedPeople):
                    exitCondition = ":)"
            charactersReplacement[validPeople] = chosenCharacter
            reasonSubbing[validPeople] = ["Groups", franchiseGroupEnd[validPeople]]
            subbedPeople.append(chosenCharacter)

            subbedPowerLevel = powerLevelsDict[people[chosenCharacter][16]]
            originalPowerLevel = powerLevelsDict[people[validPeople][16]]
            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                if adjectiveIdealValue > 4:
                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                else:
                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                    adjective = generateAdjective(adjectiveTier)
                    peopleAdjectives[chosenCharacter] = adjective
                    print("Added " + adjective + "to " + chosenCharacter + ".")

            print("Using groups, generated " + chosenCharacter + " for " + validPeople + " (" + franchiseGroupEnd[validPeople] + ")")
    replacedViaTags = []
    for person in peopleReplacementOrigs:
        if charactersReplacement[person] == "Incomplete":
            x = 1
            print("Began generating replacements for " + person + ".")
            escapeCharacter = ":("
            while escapeCharacter == ":(":
                currentPowerLevel = powerLevelsDict[people[person][16]]
                # Alright so odds:
                
                # 5% chance of full random
                # 30% odds of tags. 
                # 63% divided among the following categories (~7% individually): 
                # -Names/Aliases: Aliases, First Names, and Last Names. 
                # -Actors
                # -Role
                # -Occupation/Type
                # -Alignment
                # -Gender
                # -Race
                # -Medium
                # -Decades/Years
                # 2% of static (no change)
                RNGRandomSwapper = random.randint(1,100)

                if RNGRandomSwapper <= 3:
                    #print("Chose full random")
                    RNG = random.randint(0,len(people)-1)
                    peopleList = []
                    for person2 in people.keys():
                        peopleList.append(person2)
                    if not(peopleList[RNG] in charactersReplacement.values()) and not(peopleList[RNG] in charactersReplacement.keys()) and not(peopleList[RNG] in otherAddedCharacters) and antagonists != True and people[peopleList[RNG]][28] != "No Sub In":
                        charactersReplacement[person] = peopleList[RNG]
                        print("\tSubbing " + charactersReplacement[person] + " for " + person + " (full random)")
                        reasonSubbing[person] = ["Full Random", ""]
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                # Full random
                if RNGRandomSwapper > 3 and RNGRandomSwapper <= 35:
                    print("Replacing " + person + " with tags.")
                    rawTagList = people[person][15].split(",")
                    duoTagList = {}
                    typesOfDuoTags = []
                    tagList = {} #Dict of tags- key is the tag, value is a list of people with that tag.
                    tagName = "None"
                    for tag in rawTagList:
                        duoTag = tag.split("|")
                        if len(duoTag) > 1:
                            if not(duoTag[0] in duoTagList) and not(duoTag[1] in charactersReplacement.values()) and not (duoTag[1] in charactersReplacement.keys()) and not(duoTag[1] in otherAddedCharacters):
                                duoTagList[duoTag[0]] = []
                                typesOfDuoTags.append(duoTag[0])
                        else:
                            tagList[tag] = []
                    for character in people.keys():
                        if people[character][1] != people[person][1]:
                            subTagList = people[character][15].split(",")
                            for subTag in subTagList:
                                duoSubTag = subTag.split("|")
                                if len(duoSubTag) > 1 and duoSubTag[0] in typesOfDuoTags:
                                    duoTagList[duoSubTag[0]].append(character)
                                else:
                                    if subTag in tagList.keys():
                                        tagList[subTag].append(character)
                    #print("Duo Tag List: " + str(duoTagList))
                    #print("Tag List: " + str(tagList))
                    

                    typesOfTags = []
                    for tag in tagList.keys():
                        typesOfTags.append(tag)
                    
                    RNG = random.randint(0,3)
                    if RNG != 3 or len(typesOfDuoTags) < 1:
                        RNG = random.randint(0,len(typesOfTags)-1)
                        tagRNG = RNG
                        tagName = typesOfTags[RNG]
                        if len(tagList[typesOfTags[RNG]]) >= 1:
                            swapList = []
                            for taggedMatchee in tagList[typesOfTags[RNG]]:
                                taggedMatcheePowerLevel = powerLevelsDict[people[taggedMatchee][16]]
                                if not(taggedMatchee in charactersReplacement.values()) and not(taggedMatchee in charactersReplacement.keys()) and not(taggedMatchee in otherAddedCharacters) and taggedMatcheePowerLevel in range(0,currentPowerLevel+2):
                                    taggedMatchRarity = people[taggedMatchee][17]
                                    swapList = chooseCharacter(guildID, people, False,  taggedMatchee, taggedMatcheePowerLevel, currentPowerLevel, taggedMatchRarity, swapList)
                            if len(swapList) > 0:
                                RNG = random.randint(0,len(swapList)-1)
                                charactersReplacement[person] = swapList[RNG]
                                print("\tSubbing " + charactersReplacement[person] + " for " + person + " (tags: " + typesOfTags[tagRNG] + ")")
                                reasonSubbing[person] = ["Tags", typesOfTags[tagRNG]]

                                subbedPowerLevel = powerLevelsDict[people[swapList[RNG]][16]]
                                originalPowerLevel = powerLevelsDict[people[person][16]]

                                if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                    adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                    if adjectiveIdealValue > 4:
                                        print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                    else:
                                        adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                        adjective = generateAdjective(adjectiveTier)
                                        peopleAdjectives[swapList[RNG]] = adjective
                                        print("Added " + adjective + "to " + swapList[RNG] + ".")

                                escapeCharacter = ":)"
                                replacedViaTags.append(person)
                    else:
                        RNG = random.randint(0,len(typesOfDuoTags)-1)
                        tagRNG = RNG
                        tagName = typesOfDuoTags[RNG]
                        if len(duoTagList[typesOfDuoTags[tagRNG]]) >= 1:
                            swapList = []
                            for taggedMatchee in duoTagList[typesOfDuoTags[tagRNG]]:
                                taggedMatcheePowerLevel = powerLevelsDict[people[taggedMatchee][16]]
                                if not(taggedMatchee in charactersReplacement.values()) and not(taggedMatchee in charactersReplacement.keys()) and not(taggedMatchee in otherAddedCharacters) and taggedMatcheePowerLevel in range(0,currentPowerLevel+2):
                                    taggedMatchRarity = people[taggedMatchee][17]
                                    swapList = chooseCharacter(guildID, people, False,  taggedMatchee, taggedMatcheePowerLevel, currentPowerLevel, taggedMatchRarity, swapList)

                            if len(swapList) > 0:

                                RNG = random.randint(0,len(swapList)-1)

                                replaceCharacter = swapList[RNG]

                                secondCharactersSubRaw = []
                                secondCharactersSub = []

                                secondCharactersOrigRaw = []
                                secondCharactersOrig = []

                                for tag in people[replaceCharacter][15].split(","):
                                    tagSplit = tag.split("|")
                                    if len(tagSplit) > 1 and typesOfDuoTags[tagRNG] == tagSplit[0]:
                                        secondCharactersSubRaw.append(tagSplit[1])
                                        secondCharactersSub.append(tagSplit[1])


                                for tag in people[person][15].split(","):
                                    tagSplit = tag.split("|")
                                    if len(tagSplit) > 1 and typesOfDuoTags[tagRNG] == tagSplit[0]:
                                        secondCharactersOrigRaw.append(tagSplit[1])
                                        secondCharactersOrig.append(tagSplit[1])
                                    
                                for secondCharacter in secondCharactersOrigRaw:
                                    if not(secondCharacter in peopleReplacementOrigs) and not(secondCharacter in charactersReplacement.keys()) and not(secondCharacter in otherAddedCharacters):
                                        secondCharactersOrig.remove(secondCharacter)
                                    
                                for secondCharacter in secondCharactersSubRaw:
                                    if secondCharacter in charactersReplacement.values():
                                        secondCharactersSub.remove(secondCharacter)                         

                                finalSecondCharacter = ""
                                finalSecondCharacterSub = ""
                                if len(secondCharactersOrig) >= 1 and len(secondCharactersSub) >= 1:
                                    RNG = random.randint(0,len(secondCharactersOrig)-1)
                                    finalSecondCharacter = secondCharactersOrig[RNG]
                                    
                                    RNG = random.randint(0,len(secondCharactersSub)-1)
                                    finalSecondCharacterSub = secondCharactersSub[RNG]

                                    charactersReplacement[finalSecondCharacter] = finalSecondCharacterSub
                                    charactersReplacement[person] = replaceCharacter
                                    print("\tSubbing " + charactersReplacement[person] + " for " + person + " (duo tags: " + typesOfDuoTags[tagRNG] + ")")

                                    print("\tSubbing " + finalSecondCharacterSub + " for " + finalSecondCharacter + " (second character duo tags: " + typesOfDuoTags[tagRNG] + ")")
                                    escapeCharacter = ":)"
                                    replacedViaTags.append(person)
                                    replacedViaTags.append(finalSecondCharacter)
                                    reasonSubbing[person] = ["Group Tags (First Person)", typesOfDuoTags[tagRNG]]
                                    reasonSubbing[finalSecondCharacter] = ["Group Tags (Second Person)", typesOfDuoTags[tagRNG]]
                                    
                                    subbedPowerLevel = powerLevelsDict[people[charactersReplacement[person]][16]]
                                    originalPowerLevel = powerLevelsDict[people[person][16]]

                                    if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                        adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                        if adjectiveIdealValue > 4:
                                            print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                        else:
                                            adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                            adjective = generateAdjective(adjectiveTier)
                                            peopleAdjectives[charactersReplacement[person]] = adjective
                                            print("Added " + adjective + "to " + charactersReplacement[person] + ".")

                                    subbedPowerLevel = powerLevelsDict[people[finalSecondCharacterSub][16]]
                                    originalPowerLevel = powerLevelsDict[people[finalSecondCharacter][16]]

                                    if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                        adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                        if adjectiveIdealValue > 4:
                                            print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                        else:
                                            adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                            adjective = generateAdjective(adjectiveTier)
                                            peopleAdjectives[finalSecondCharacterSub] = adjective
                                            print("Added " + adjective + "to " + finalSecondCharacterSub + ".")

                    
                    #if escapeCharacter != ":)":
                        #print("Tags failed (" + tagName + " had no matches.)")
                # Tags
                if RNGRandomSwapper > 35 and RNGRandomSwapper <= 42:
                    print("Replacing " + person + " with names.")

                    namesChecked = ["First", "Last", "Aliases"]
                    subCharacter = "None"
                    nameShared = ""
                    while len(namesChecked) > 0 and subCharacter == "None":
                        RNG = random.randint(0,len(namesChecked)-1)
                        randomName = namesChecked[RNG]
                        if randomName == "First":
                            #print("First Name Start!")
                            firstName = people[person][5]
                            if firstName != "":
                                nameSharers = []
                                for character in people.keys():
                                    characterPowerLevel = powerLevelsDict[people[character][16]]
                                    if people[character][5] == firstName and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                        taggedMatchRarity = people[character][17]
                                        nameSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, nameSharers)
                                if len(nameSharers) >= 1:
                                    RNG = random.randint(0,len(nameSharers)-1)
                                    subCharacter = nameSharers[RNG]
                                    
                                    nameShared = firstName
                                else:
                                    namesChecked.remove("First")
                            else:
                                namesChecked.remove("First")

                            #print("First Name Complete!")
                        if randomName == "Last":
                            #print("Last Name Start!")
                            lastName = people[person][6]
                            if lastName != "":
                                nameSharers = []
                                for character in people.keys():
                                    characterPowerLevel = powerLevelsDict[people[character][16]]
                                    if people[character][6] == lastName and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                        taggedMatchRarity = people[character][17]
                                        nameSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, nameSharers)

                                if len(nameSharers) >= 1:
                                    RNG = random.randint(0,len(nameSharers)-1)
                                    subCharacter = nameSharers[RNG]
                                    nameShared = lastName
                                else:
                                    namesChecked.remove("Last")
                            else:
                                namesChecked.remove("Last")
                            #print("Last name complete!")
                        if randomName == "Aliases":
                            #print("Alias start!")
                            aliases = people[person][7].split("|")
                            nameSharers = []
                            for character in people.keys():
                                subCharacterAliases = people[character][7].split("|")
                                for subAlias in subCharacterAliases:
                                    characterPowerLevel = powerLevelsDict[people[character][16]]
                                    if subAlias in aliases and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                        taggedMatchRarity = people[character][17]
                                        nameSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, nameSharers)
                            if len(nameSharers) >= 1:
                                RNG = random.randint(0,len(nameSharers)-1)
                                subCharacter = nameSharers[RNG]
                                subCharacterAliases = people[subCharacter][7].split("|")
                                for subCharAlias in subCharacterAliases:
                                    if subCharAlias in aliases:
                                        nameShared = subCharAlias                            
                            else:
                                namesChecked.remove("Aliases")
                            #print("Alias complete!")
                    if subCharacter != "None":
                        print("\tSubbing " + subCharacter + " for " + person + " (names: " + nameShared + ")")
                        reasonSubbing[person] = ["Names", nameShared]
                        charactersReplacement[person] = subCharacter

                        subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                        originalPowerLevel = powerLevelsDict[people[person][16]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                peopleAdjectives[subCharacter] = adjective
                                print("Added " + adjective + "to " + subCharacter + ".")

                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    #else:
                        #print("Names were an ultimate failure.")
                # Names
                if RNGRandomSwapper > 42 and RNGRandomSwapper <= 49:
                    print("Replacing " + person + " with actors.")

                    actors = people[person][8].split("|")
                    actorSharers = []
                    actorList = []
                    subCharacter = "None"
                    actorFinal = ""
                    if people[person][8] != "":
                        for character in people.keys():
                            subCharacterActors = people[character][8].split("|")
                            for subActor in subCharacterActors:
                                characterPowerLevel = powerLevelsDict[people[character][16]]
                                if subActor in actors and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                    taggedMatchRarity = people[character][17]
                                    actorSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, actorSharers)
                                    actorList = chooseCharacter(guildID, people, True,  subActor, characterPowerLevel, currentPowerLevel, taggedMatchRarity, actorList)
                    if len(actorSharers) >= 1:
                        RNG = random.randint(0,len(actorSharers)-1)
                        subCharacter = actorSharers[RNG]
                        actorFinal = actorList[RNG]
                    if subCharacter != "None":
                        print("\tSubbing " + subCharacter + " for " + person + " (actors: " + actorFinal + ")")
                        reasonSubbing[person] = ["Actors", actorFinal]
                        charactersReplacement[person] = subCharacter

                        subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                        originalPowerLevel = powerLevelsDict[people[person][16]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                peopleAdjectives[subCharacter] = adjective
                                print("Added " + adjective + "to " + subCharacter + ".")

                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    #else:
                        #print("Actors were an ultimate failure.")
                # Actors
                if RNGRandomSwapper > 49 and RNGRandomSwapper <= 56:
                    print("Replacing " + person + " with type/occupation.")
                    
                    role = people[person][10]
                    if role != "":
                        roleSharers = []
                        for character in people.keys():
                            characterPowerLevel = powerLevelsDict[people[character][16]]

                            if people[character][10] == role and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                actorSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, roleSharers)
                        if len(roleSharers) >= 1:
                            RNG = random.randint(0,len(roleSharers)-1)
                            subCharacter = roleSharers[RNG]
                            print("\tSubbing " + subCharacter + " for " + person + " (types: " + role + ")")
                            reasonSubbing[person] = ["Type", role]
                            
                            charactersReplacement[person] = subCharacter

                            subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                            originalPowerLevel = powerLevelsDict[people[person][16]]
                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    peopleAdjectives[subCharacter] = adjective
                                    print("Added " + adjective + "to " + subCharacter + ".")
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                # Type
                if RNGRandomSwapper > 56 and RNGRandomSwapper <= 63:
                    print("Replacing " + person + " with role.")
                    
                    role = people[person][13]
                    if role != "":
                        roleSharers = []
                        for character in people.keys():
                            characterPowerLevel = powerLevelsDict[people[character][16]]

                            if people[character][13] == role and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                roleSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, roleSharers)
                        if len(roleSharers) >= 1:
                            RNG = random.randint(0,len(roleSharers)-1)
                            subCharacter = roleSharers[RNG]
                            print("\tSubbing " + subCharacter + " for " + person + " (roles: " + role + ")")
                            reasonSubbing[person] = ["Roles", role]
                            charactersReplacement[person] = subCharacter
                            subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                            originalPowerLevel = powerLevelsDict[people[person][16]]
                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    peopleAdjectives[subCharacter] = adjective
                                    print("Added " + adjective + "to " + subCharacter + ".")
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                # Role
                if RNGRandomSwapper > 63 and RNGRandomSwapper <= 70:
                    print("Replacing " + person + " with alignment.")
                    
                    alignment = people[person][12]
                    if alignment != "":
                        alignmentShared = []
                        for character in people.keys():
                            characterPowerLevel = powerLevelsDict[people[character][16]]

                            if people[character][12] == alignment and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                alignmentShared = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, alignmentShared)
                        if len(alignmentShared) >= 1:
                            RNG = random.randint(0,len(alignmentShared)-1)
                            subCharacter = alignmentShared[RNG]
                            print("\tSubbing " + subCharacter + " for " + person + " (alignment: " + alignment + ")")
                            reasonSubbing[person] = ["Alignment", alignment]
                            charactersReplacement[person] = subCharacter
                            subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                            originalPowerLevel = powerLevelsDict[people[person][16]]
                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    peopleAdjectives[subCharacter] = adjective
                                    print("Added " + adjective + "to " + subCharacter + ".")
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                # Alignment
                if RNGRandomSwapper > 70 and RNGRandomSwapper <= 77:
                    print("Replacing " + person + " with gender.")
                    
                    gender = people[person][14]
                    if gender != "":
                        genderShared = []
                        for character in people.keys():
                            characterPowerLevel = powerLevelsDict[people[character][16]]
                            if people[character][14] == gender and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                genderShared = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, genderShared)
                        if len(genderShared) >= 1:
                            RNG = random.randint(0,len(genderShared)-1)
                            subCharacter = genderShared[RNG]
                            print("\tSubbing " + subCharacter + " for " + person + " (gender: " + gender + ")")
                            reasonSubbing[person] = ["Gender", gender]
                            charactersReplacement[person] = subCharacter
                            subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                            originalPowerLevel = powerLevelsDict[people[person][16]]
                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    peopleAdjectives[subCharacter] = adjective
                                    print("Added " + adjective + "to " + subCharacter + ".")
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                # Gender
                if RNGRandomSwapper > 77 and RNGRandomSwapper <= 84:
                    print("Replacing " + person + " with race.")
                    
                    race = people[person][11]
                    if race != "":
                        raceShared = []
                        for character in people.keys():
                            characterPowerLevel = powerLevelsDict[people[character][16]]

                            if people[character][11] == race and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                raceShared = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, raceShared)

                        if len(raceShared) >= 1:
                            RNG = random.randint(0,len(raceShared)-1)
                            subCharacter = raceShared[RNG]
                            print("\tSubbing " + subCharacter + " for " + person + " (race: " + race + ")")
                            reasonSubbing[person] = ["Race", race]
                            charactersReplacement[person] = subCharacter
                            subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                            originalPowerLevel = powerLevelsDict[people[person][16]]
                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    peopleAdjectives[subCharacter] = adjective
                                    print("Added " + adjective + "to " + subCharacter + ".")
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                # Race
                if RNGRandomSwapper > 84 and RNGRandomSwapper <= 91:
                    print("Replacing " + person + " with medium.")

                    mediums = people[person][20].split(",")
                    mediumSharers = []
                    mediumList = []
                    subCharacter = "None"
                    mediumFinal = ""
                    for character in people.keys():
                        subCharacterMediums = people[character][20].split(",")
                        for subMedium in subCharacterMediums:
                            characterPowerLevel = powerLevelsDict[people[character][16]]
                            if subMedium in mediums and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                taggedMatchRarity = people[character][17]
                                mediumSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, mediumSharers)
                                mediumList = chooseCharacter(guildID, people, True, subMedium, characterPowerLevel, currentPowerLevel, taggedMatchRarity, mediumList)
                    if len(mediumSharers) >= 1:
                        RNG = random.randint(0,len(mediumSharers)-1)
                        subCharacter = mediumSharers[RNG]
                        mediumFinal = mediumList[RNG]
                    if subCharacter != "None":
                        print("\tSubbing " + subCharacter + " for " + person + " (medium: " + mediumFinal + ")")
                        reasonSubbing[person] = ["Mediums", mediumFinal]
                        charactersReplacement[person] = subCharacter
                        subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                        originalPowerLevel = powerLevelsDict[people[person][16]]
                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                peopleAdjectives[subCharacter] = adjective
                                print("Added " + adjective + "to " + subCharacter + ".")
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    #else:
                        #print("Mediums were an ultimate failure.")
                # Medium
                if RNGRandomSwapper > 91 and RNGRandomSwapper <= 98:
                    print("Replacing " + person + " with age.")
                    namesChecked = ["Years", "Decades"]
                    subCharacter = "None"
                    ageShared = ""
                    ageType = ""
                    if people[person][9] != "":
                        while len(namesChecked) > 0 and subCharacter == "None":
                            RNG = random.randint(0,len(namesChecked)-1)
                            randomName = namesChecked[RNG]
                            if randomName == "Years":
                                #print("First Name Start!")
                                years = people[person][9].split("|")[0]
                                if years != "":
                                    yearsSharers = []
                                    for character in people.keys():
                                        characterPowerLevel = powerLevelsDict[people[character][16]]
                                        if people[character][9].split("|")[0] == years and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                            taggedMatchRarity = people[character][17]
                                            yearsSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, yearsSharers)

                                    if len(yearsSharers) >= 1:
                                        RNG = random.randint(0,len(yearsSharers)-1)
                                        subCharacter = yearsSharers[RNG]
                                        ageShared = years
                                        ageType = "Years"
                                    else:
                                        namesChecked.remove("Years")
                                else:
                                    namesChecked.remove("Years")

                                #print("First Name Complete!")
                            if randomName == "Decades":
                                #print("Last Name Start!")
                                decades = people[person][9].split("|")[1]
                                if decades != "":
                                    decadeSharers = []
                                    for character in people.keys():
                                        if people[character][9] != "":
                                            characterPowerLevel = powerLevelsDict[people[character][16]]
                                            if people[character][9].split("|")[1] == decades and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters) and characterPowerLevel in range(0,currentPowerLevel+2):
                                                taggedMatchRarity = people[character][17]
                                                decadeSharers = chooseCharacter(guildID, people, False,  character, characterPowerLevel, currentPowerLevel, taggedMatchRarity, decadeSharers)

                                    if len(decadeSharers) >= 1:
                                        RNG = random.randint(0,len(decadeSharers)-1)
                                        subCharacter = decadeSharers[RNG]
                                        ageShared = decades
                                        ageType = "Decades"
                                    else:
                                        namesChecked.remove("Decades")
                                else:
                                    namesChecked.remove("Decades")
                                #print("Last name complete!")
                                    #print("Alias complete!")
                    if subCharacter != "None":
                        print("\tSubbing " + subCharacter + " for " + person + " (years: " + ageShared + " (" + ageType + ")" + ")")
                        reasonSubbing[person] = ["Ages", ageType + "|" + ageShared]
                        charactersReplacement[person] = subCharacter
                        
                        subbedPowerLevel = powerLevelsDict[people[subCharacter][16]]
                        originalPowerLevel = powerLevelsDict[people[person][16]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                peopleAdjectives[subCharacter] = adjective
                                print("Added " + adjective + "to " + subCharacter + ".")

                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    #else:
                        #print("Ages were an ultimate failure.")
                # Age
                if RNGRandomSwapper > 98:
                    print(person + " stays the same")

                    charactersReplacement[person] = person
                    print("Not subbing " + charactersReplacement[person] + " for " + person + " (no change)")
                    reasonSubbing[person] = ["No Change", ""]
                    
                    escapeCharacter = ":)"
                    replacedViaTags.append(person)
                # Static
                if escapeCharacter == ":(":
                    print("\tGeneration #" + str(x) + " failed, attempting again.")
                    x+=1
    for character in charactersReplacement.keys():
        otherAddedCharacters.append(character)
    for character in charactersReplacement.values():
        otherAddedCharacters.append(character)
    print("Completed Generation!\n")
    return [charactersReplacement, reasonSubbing, otherAddedCharacters, peopleAdjectives]

def genMinions(franchiseName, franchiseInfo, guildID):
    print("Generating Minions!")
    origMinions = franchiseInfo[9].split("|")
    minions = allMinions()
    people = minions
    replacements = {}
    reasonsForSubs = {}
    minionAdjectives = {}

    for origMinion in origMinions:
        replacements[origMinion] = ";)"

    for origMinion in origMinions: 
        RNG = random.randint(1,4)
        if RNG == 4:
            escapeCharacter = ":("
            while escapeCharacter == ":(":
                minionsInfo = minions[origMinion]
                connectedMinions = []
                if minionsInfo[6] != "":
                    for connectedGroup in minionsInfo[6].split("|"):
                        connectedMinions.append(connectedGroup)

                RNGPicker = random.randint(1,100)
                if RNGPicker <= 5:
                    subMinionList = []
                    for subMinion in minions.keys():
                        if subMinion != origMinion and not(subMinion in connectedMinions):
                            subMinionList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[minions[subMinion][13]], powerLevelsDict[minionsInfo[13]], minions[subMinion][14], subMinionList)
                    print("Length of subMinionList: " + str(len(subMinionList)))
                    RNG = 0
                    if len(subMinionList) > 1:
                        RNG = random.randint(0,len(subMinionList)-1)

                    replacements[origMinion] = subMinionList[RNG]
                    reasonsForSubs[origMinion] = ["Full Random"]
                    subMinionInfo = minions[subMinionList[RNG]]

                    subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                    originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                    if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                        adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                        if adjectiveIdealValue > 4:
                            print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                        else:
                            adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                            adjective = generateAdjective(adjectiveTier)
                            minionAdjectives[origMinion] = adjective
                            print("Added " + adjective + "to " + origMinion + ".")

                    escapeCharacter = ":)"
                # Full Random
                if RNGPicker > 5 and RNGPicker <= 40:
                    tags = {}
                    tagList = minionsInfo[12].split(",")
                    for tag in tagList:
                        tags[tag] = []
                    
                    x = 0
                    for subMinion in minions.keys():
                        subMinionTags = minions[subMinion][12].split(",")
                        for subTag in subMinionTags:
                            try:
                                tags[subTag].append(subMinion)
                            except:
                                x+=1
                                
                    
                    for tag in tags:
                        if len(tags[tag]) == 0:
                            del(tags[tag])
                    
                    #print("Tags: " + str(tags))
                    if len(tags.keys()) > 0:
                        RNG = 0
                        if len(tags.keys()) > 1:
                            RNG = random.randint(0,len(tags.keys())-1)
                        tagList = []
                        for tag in tags.keys():
                            tagList.append(tag)
                        
                        chosenTag = tagList[RNG]
                        swapList = []
                        for subMinion in tags[chosenTag]:
                            subMinionInfo = minions[subMinion]
                            if subMinion != origMinion and not(subMinion in connectedMinions):
                                swapList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[subMinionInfo[13]], powerLevelsDict[minionsInfo[13]], subMinionInfo[14], swapList)
                        if len(swapList) > 0:
                            if len(swapList) > 1:
                                RNG = random.randint(0,len(swapList)-1)
                            else:
                                RNG = 0
                            chosenMinion = swapList[RNG]
                            print("Tags: substituting " + chosenMinion + " for " + origMinion + " (" + chosenTag + ")")
                            replacements[origMinion] = chosenMinion
                            reasonsForSubs[origMinion] = ["Tags", chosenTag]

                            subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                            originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    minionAdjectives[origMinion] = adjective
                                    print("Added " + adjective + "to " + origMinion + ".")

                            escapeCharacter = ":)"
                # Tags
                if RNGPicker > 40 and RNGPicker <= 55:
                    typeList = []
                    for subMinion in minions.keys():
                        if minions[subMinion][9] == minionsInfo[9] and subMinion != origMinion and not(subMinion in connectedMinions):
                            typeList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[minions[subMinion][13]], powerLevelsDict[minionsInfo[13]], minions[subMinion][14], typeList)

                    if len(typeList) > 0:
                        if len(typeList) > 1:
                            RNG = random.randint(0,len(typeList)-1)
                        else: 
                            RNG = 0

                        subMinionList = []
                        for subMinion in minions.keys():
                            subMinionList.append(subMinion)

                        replacements[origMinion] = typeList[RNG]
                        reasonsForSubs[origMinion] = ["Types", minionsInfo[9]]
                        subMinionInfo = minions[typeList[RNG]]

                        subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                        originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                minionAdjectives[origMinion] = adjective
                                print("Added " + adjective + "to " + origMinion + ".")

                        escapeCharacter = ":)"                
                # Type
                if RNGPicker > 55 and RNGPicker <= 70:
                    raceList = []
                    for subMinion in minions.keys():
                        if minions[subMinion][10] == minionsInfo[10] and subMinion != origMinion and not(subMinion in connectedMinions):
                            raceList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[minions[subMinion][13]], powerLevelsDict[minionsInfo[13]], minions[subMinion][14], raceList)
                    if len(raceList) > 0:
                        if len(raceList) > 1:
                            RNG = random.randint(0,len(raceList)-1)
                        else: 
                            RNG = 0

                        subMinionList = []
                        for subMinion in minions.keys():
                            subMinionList.append(subMinion)

                        replacements[origMinion] = raceList[RNG]
                        reasonsForSubs[origMinion] = ["Races", minionsInfo[10]]
                        subMinionInfo = minions[raceList[RNG]]

                        subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                        originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                minionAdjectives[origMinion] = adjective
                                print("Added " + adjective + "to " + origMinion + ".")

                        escapeCharacter = ":)"                   
                # Race
                if RNGPicker > 70 and RNGPicker <= 85:
                    alignList = []
                    for subMinion in minions.keys():
                        if minions[subMinion][11] == minionsInfo[11] and subMinion != origMinion and not(subMinion in connectedMinions):
                            alignList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[minions[subMinion][13]], powerLevelsDict[minionsInfo[13]], minions[subMinion][14], alignList)

                    if len(alignList) > 0:
                        if len(alignList) > 1:
                            RNG = random.randint(0,len(alignList)-1)
                        else:
                            RNG = 0

                        subMinionList = []
                        for subMinion in minions.keys():
                            subMinionList.append(subMinion)

                        replacements[origMinion] = alignList[RNG]
                        reasonsForSubs[origMinion] = ["Alignment", minionsInfo[11]]
                        subMinionInfo = minions[alignList[RNG]]

                        subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                        originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                        if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                            adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                            if adjectiveIdealValue > 4:
                                print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                            else:
                                adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                adjective = generateAdjective(adjectiveTier)
                                minionAdjectives[origMinion] = adjective
                                print("Added " + adjective + "to " + origMinion + ".")

                        escapeCharacter = ":)"                    
                # Alignment
                if RNGPicker > 85 and RNGPicker <= 100:
                    mediums = {}
                    for medium in minionsInfo[16].split(","):
                        newMediumList = []
                        for subMinion in minions.keys():
                            if medium in minions[subMinion][16].split(",") and subMinion != origMinion and not(subMinion in connectedMinions):
                                newMediumList = chooseCharacter(guildID, people, False,  subMinion, powerLevelsDict[minions[subMinion][13]], powerLevelsDict[minionsInfo[13]], minions[subMinion][14], newMediumList)
                        mediums[medium] = newMediumList
                    
                    mediers = []
                    for medB in mediums.keys():
                        mediers.append(medB)

                    for medium in mediers:
                        if len(mediums[medium]) > 1:
                            del mediums[medium]

                    listOfMediums = []
                    for medium in mediums.keys():
                        listOfMediums.append(medium)
                    
                    if len(listOfMediums) > 0:
                        if len(listOfMediums) > 1:
                            RNG = random.randint(0,len(listOfMediums)-1)
                        else:
                            RNG = 0
                        chosenMedium = listOfMediums[RNG]

                        personList = mediums[chosenMedium]
                        if len(personList) > 0:
                            if len(personList) > 1:
                                RNG = random.randint(0,len(personList)-1)
                            else:
                                RNG = 0
                            chosenPerson = personList[RNG]

                            replacements[origMinion] = chosenPerson
                            reasonsForSubs[origMinion] = ["Medium", chosenMedium]
                            subMinionInfo = minions[chosenPerson]

                            subbedPowerLevel = powerLevelsDict[subMinionInfo[13]]
                            originalPowerLevel = powerLevelsDict[minionsInfo[13]]

                            if subbedPowerLevel < originalPowerLevel and originalPowerLevel-subbedPowerLevel > 1:
                                adjectiveIdealValue = originalPowerLevel-subbedPowerLevel
                                if adjectiveIdealValue > 4:
                                    print("Failed substitution due to the power level difference being " + str(adjectiveIdealValue) + "! Send help please!")
                                else:
                                    adjectiveTier = additionalPowerLevels[adjectiveIdealValue]
                                    adjective = generateAdjective(adjectiveTier)
                                    minionAdjectives[origMinion] = adjective
                                    print("Added " + adjective + "to " + origMinion + ".")
                            escapeCharacter = ":)"       
                # Medium
        else:
            replacements[origMinion] = origMinion
            reasonsForSubs[origMinion] = ["No Change"]
    print("Completed Generation!\n")

    return [replacements, reasonsForSubs, minionAdjectives]
