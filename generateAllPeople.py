import random
import os
from all import allFranchises
from all import allGroups
from all import allPeople


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 
def genAllPeople(peopleReplacementOrigs, franchiseInfo, otherAddedCharacters):
    print("People Replace: " + str(peopleReplacementOrigs))
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

    for person in peopleReplacementOrigs:
        print("<" + person + ">")

        if person != "":
            print(str(people[person]))
            groupsPerson = people[person][18].split(",")
            for group in groupsPerson:
                if not(group in groupsCanReplace) and group != "":
                    groupsCanReplace.append(group)
                    endValidGroups.append(group)
    # This makes groupsCanReplace (and, by extension, endValidGroups) a full list of all the groups in all the people in the franchise
    # file. 
    if groupReplacementRNG == 4 and len(groupsCanReplace) > 0:

        for group in endValidGroups:
            for personGroupMember in franchiseGroups[group]:
                if not(personGroupMember in peopleReplacementOrigs) and group in groupsCanReplace:
                    print("Removed " + group + " because of the exclusion of " + personGroupMember)
                    groupsCanReplace.remove(group)
                if len(franchiseGroups[group]) <= 1:
                    print("Removed " + group + " because of the membership of only " + personGroupMember)
                    groupsCanReplace.remove(group)
        # Now, this bit removes all the people that aren't valid, either because the group only has one person in it or because somebody in
        # the group isn't in the current replace Franchise. 
        print("\n")
        testString = ""
        for group in groupsCanReplace:
            testString = testString + group + ", "
        testString = testString[0:len(testString)-2:]
        print("For " + franchiseInfo[0] + ", " + str(len(groupsCanReplace)) + " groups were found in total. (" + testString + ")")
        
        # This is just a little method that prints out the groups at this stage in the process. 
        
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
                if groups[group] == len(franchiseGroups[validGroup]):
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
                            #print("Removed " + groupRemove + " from " + personRemoval)      
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
            print("Using groups, generated " + chosenCharacter + " for " + validPeople + " (" + franchiseGroupEnd[validPeople] + ")")
    replacedViaTags = []
    for person in peopleReplacementOrigs:
        if charactersReplacement[person] == "Incomplete":
            escapeCharacter = ":("
            while escapeCharacter == ":(":
                
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

                if RNGRandomSwapper <= 5:
                    print("Replacing " + person + " with full random")

                    RNG = random.randint(0,len(people)-1)
                    peopleList = []
                    for person2 in people.keys():
                        peopleList.append(person2)
                    if not(peopleList[RNG] in charactersReplacement.values()) and not(peopleList[RNG] in charactersReplacement.keys()) and not(peopleList[RNG] in otherAddedCharacters):
                        charactersReplacement[person] = peopleList[RNG]
                        print("Subbing " + charactersReplacement[person] + " for " + person + " (full random)")
                        reasonSubbing[person] = ["Full Random", ""]
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                if RNGRandomSwapper > 5 and RNGRandomSwapper <= 35:
                    print("Replacing " + person + " with tags.")
                    #Occasionally adds a seocnd person when group tags.
                    rawTagList = people[person][15].split(",")
                    duoTagList = {}
                    typesOfDuoTags = []
                    tagList = {}
                    tagName = "None"
                    for tag in rawTagList:
                        duoTag = tag.split("|")
                        if len(duoTag) > 1:
                            if not(duoTag[0] in duoTagList):
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
                                if not(taggedMatchee in charactersReplacement.values()) and not(taggedMatchee in charactersReplacement.keys()) and not(taggedMatchee in otherAddedCharacters):
                                    taggedMatchRarity = people[taggedMatchee][17]
                                    if taggedMatchRarity == "Low":
                                        swapList.append(taggedMatchee)
                                    if taggedMatchRarity == "Medium":
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
                                    if taggedMatchRarity == "High":
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
                            if len(swapList) > 0:
                                RNG = random.randint(0,len(swapList)-1)
                                charactersReplacement[person] = swapList[RNG]
                                print("Subbing " + charactersReplacement[person] + " for " + person + " (tags: " + typesOfTags[tagRNG] + ")")
                                reasonSubbing[person] = ["Tags", typesOfTags[tagRNG]]

                                escapeCharacter = ":)"
                                replacedViaTags.append(person)
                    else:
                        RNG = random.randint(0,len(typesOfDuoTags)-1)
                        tagRNG = RNG
                        tagName = typesOfDuoTags[RNG]

                        if len(duoTagList[typesOfDuoTags[tagRNG]]) >= 1:
                            swapList = []
                            for taggedMatchee in duoTagList[typesOfDuoTags[tagRNG]]:
                                if not(taggedMatchee in charactersReplacement.values()) and not(taggedMatchee in charactersReplacement.keys()) and not(taggedMatchee in otherAddedCharacters):
                                    taggedMatchRarity = people[taggedMatchee][17]
                                    if taggedMatchRarity == "Low":
                                        swapList.append(taggedMatchee)
                                    if taggedMatchRarity == "Medium":
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
                                    if taggedMatchRarity == "High":
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
                                        swapList.append(taggedMatchee)
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
                                    print("Subbing " + charactersReplacement[person] + " for " + replaceCharacter + " (duo tags: " + typesOfDuoTags[tagRNG] + ")")

                                    print("Subbing " + finalSecondCharacterSub + " for " + finalSecondCharacter + " (second character duo tags: " + typesOfDuoTags[tagRNG] + ")")
                                    escapeCharacter = ":)"
                                    replacedViaTags.append(person)
                                    replacedViaTags.append(finalSecondCharacter)
                                    reasonSubbing[person] = ["Group Tags (First Person)", typesOfDuoTags[tagRNG]]
                                    reasonSubbing[finalSecondCharacter] = ["Group Tags (Second Person)", typesOfDuoTags[tagRNG]]


                    
                    #if escapeCharacter != ":)":
                        #print("Tags failed (" + tagName + " had no matches.)")
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
                                    if people[character][5] == firstName and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                        taggedMatchRarity = people[character][17]
                                        if taggedMatchRarity == "Low":
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "Medium":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "High":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                            nameSharers.append(character)
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
                                    if people[character][6] == lastName and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                        taggedMatchRarity = people[character][17]
                                        if taggedMatchRarity == "Low":
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "Medium":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "High":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                            nameSharers.append(character)
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
                                    if subAlias in aliases and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                        taggedMatchRarity = people[character][17]
                                        if taggedMatchRarity == "Low":
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "Medium":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                        if taggedMatchRarity == "High":
                                            nameSharers.append(character)
                                            nameSharers.append(character)
                                            nameSharers.append(character)
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
                        print("Subbing " + subCharacter + " for " + person + " (names: " + nameShared + ")")
                        reasonSubbing[person] = ["Names", nameShared]
                        charactersReplacement[person] = subCharacter

                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    else:
                        print("Names were an ultimate failure.")
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
                                if subActor in actors and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                    taggedMatchRarity = people[character][17]
                                    if taggedMatchRarity == "Low":
                                        actorSharers.append(character)
                                        actorList.append(subActor)
                                    if taggedMatchRarity == "Medium":
                                        actorSharers.append(character)
                                        actorSharers.append(character)
                                        actorList.append(subActor)
                                        actorList.append(subActor)
                                    if taggedMatchRarity == "High":
                                        actorSharers.append(character)
                                        actorSharers.append(character)
                                        actorSharers.append(character)

                                        actorList.append(subActor)
                                        actorList.append(subActor)
                                        actorList.append(subActor)
                    if len(actorSharers) >= 1:
                        RNG = random.randint(0,len(actorSharers)-1)
                        subCharacter = actorSharers[RNG]
                        actorFinal = actorList[RNG]
                    if subCharacter != "None":
                        print("Subbing " + subCharacter + " for " + person + " (actors: " + actorFinal + ")")
                        reasonSubbing[person] = ["Actors", actorFinal]
                        charactersReplacement[person] = subCharacter
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    else:
                        print("Actors were an ultimate failure.")
                if RNGRandomSwapper > 49 and RNGRandomSwapper <= 56:
                    print("Replacing " + person + " with type/occupation.")
                    
                    role = people[person][10]
                    if role != "":
                        roleSharers = []
                        for character in people.keys():
                            if people[character][10] == role and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    roleSharers.append(character)
                                if taggedMatchRarity == "Medium":
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                                if taggedMatchRarity == "High":
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                        if len(roleSharers) >= 1:
                            RNG = random.randint(0,len(roleSharers)-1)
                            subCharacter = roleSharers[RNG]
                            print("Subbing " + subCharacter + " for " + person + " (types: " + role + ")")
                            reasonSubbing[person] = ["Type", role]
                            charactersReplacement[person] = subCharacter
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                if RNGRandomSwapper > 56 and RNGRandomSwapper <= 63:
                    print("Replacing " + person + " with role.")
                    
                    role = people[person][13]
                    if role != "":
                        roleSharers = []
                        for character in people.keys():
                            if people[character][13] == role and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    roleSharers.append(character)
                                if taggedMatchRarity == "Medium":
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                                if taggedMatchRarity == "High":
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                                    roleSharers.append(character)
                        if len(roleSharers) >= 1:
                            RNG = random.randint(0,len(roleSharers)-1)
                            subCharacter = roleSharers[RNG]
                            print("Subbing " + subCharacter + " for " + person + " (roles: " + role + ")")
                            reasonSubbing[person] = ["Roles", role]
                            charactersReplacement[person] = subCharacter
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                if RNGRandomSwapper > 63 and RNGRandomSwapper <= 70:
                    print("Replacing " + person + " with alignment.")
                    
                    alignment = people[person][12]
                    if alignment != "":
                        alignmentShared = []
                        for character in people.keys():
                            if people[character][12] == alignment and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    alignmentShared.append(character)
                                if taggedMatchRarity == "Medium":
                                    alignmentShared.append(character)
                                    alignmentShared.append(character)
                                if taggedMatchRarity == "High":
                                    alignmentShared.append(character)
                                    alignmentShared.append(character)
                                    alignmentShared.append(character)
                        if len(alignmentShared) >= 1:
                            RNG = random.randint(0,len(alignmentShared)-1)
                            subCharacter = alignmentShared[RNG]
                            print("Subbing " + subCharacter + " for " + person + " (alignment: " + alignment + ")")
                            reasonSubbing[person] = ["Alignment", alignment]
                            charactersReplacement[person] = subCharacter
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                if RNGRandomSwapper > 70 and RNGRandomSwapper <= 77:
                    print("Replacing " + person + " with gender.")
                    
                    gender = people[person][14]
                    if gender != "":
                        genderShared = []
                        for character in people.keys():
                            if people[character][14] == gender and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    genderShared.append(character)
                                if taggedMatchRarity == "Medium":
                                    genderShared.append(character)
                                    genderShared.append(character)
                                if taggedMatchRarity == "High":
                                    genderShared.append(character)
                                    genderShared.append(character)
                                    genderShared.append(character)
                        if len(genderShared) >= 1:
                            RNG = random.randint(0,len(genderShared)-1)
                            subCharacter = genderShared[RNG]
                            print("Subbing " + subCharacter + " for " + person + " (gender: " + gender + ")")
                            reasonSubbing[person] = ["Gender", gender]
                            charactersReplacement[person] = subCharacter
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
                if RNGRandomSwapper > 77 and RNGRandomSwapper <= 84:
                    print("Replacing " + person + " with race.")
                    
                    race = people[person][11]
                    if race != "":
                        raceShared = []
                        for character in people.keys():
                            if people[character][11] == race and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    raceShared.append(character)
                                if taggedMatchRarity == "Medium":
                                    raceShared.append(character)
                                    raceShared.append(character)
                                if taggedMatchRarity == "High":
                                    raceShared.append(character)
                                    raceShared.append(character)
                                    raceShared.append(character)
                        if len(raceShared) >= 1:
                            RNG = random.randint(0,len(raceShared)-1)
                            subCharacter = raceShared[RNG]
                            print("Subbing " + subCharacter + " for " + person + " (race: " + race + ")")
                            reasonSubbing[person] = ["Race", race]
                            charactersReplacement[person] = subCharacter
                            escapeCharacter = ":)"
                            replacedViaTags.append(person)
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
                            if subMedium in mediums and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                taggedMatchRarity = people[character][17]
                                if taggedMatchRarity == "Low":
                                    mediumSharers.append(character)
                                    mediumList.append(subMedium)
                                if taggedMatchRarity == "Medium":
                                    mediumSharers.append(character)
                                    mediumSharers.append(character)
                                    mediumList.append(subMedium)
                                    mediumList.append(subMedium)
                                if taggedMatchRarity == "High":
                                    mediumSharers.append(character)
                                    mediumSharers.append(character)
                                    mediumSharers.append(character)

                                    mediumList.append(subMedium)
                                    mediumList.append(subMedium)
                                    mediumList.append(subMedium)
                    if len(mediumSharers) >= 1:
                        RNG = random.randint(0,len(mediumSharers)-1)
                        subCharacter = mediumSharers[RNG]
                        mediumFinal = mediumList[RNG]
                    if subCharacter != "None":
                        print("Subbing " + subCharacter + " for " + person + " (actors: " + mediumFinal + ")")
                        reasonSubbing[person] = ["Mediums", mediumFinal]
                        charactersReplacement[person] = subCharacter
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    else:
                        print("Mediums were an ultimate failure.")
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
                                        if people[character][9].split("|")[0] == years and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                            taggedMatchRarity = people[character][17]
                                            if taggedMatchRarity == "Low":
                                                yearsSharers.append(character)
                                            if taggedMatchRarity == "Medium":
                                                yearsSharers.append(character)
                                                yearsSharers.append(character)
                                            if taggedMatchRarity == "High":
                                                yearsSharers.append(character)
                                                yearsSharers.append(character)
                                                yearsSharers.append(character)
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
                                            if people[character][9].split("|")[1] == decades and character != person and not(character in charactersReplacement.values()) and not(character in charactersReplacement.keys()) and not(character in otherAddedCharacters):
                                                print(people[character][9].split("|")[1] + "/" + decades)
                                                taggedMatchRarity = people[character][17]
                                                if taggedMatchRarity == "Low":
                                                    decadeSharers.append(character)
                                                if taggedMatchRarity == "Medium":
                                                    decadeSharers.append(character)
                                                    decadeSharers.append(character)
                                                if taggedMatchRarity == "High":
                                                    decadeSharers.append(character)
                                                    decadeSharers.append(character)
                                                    decadeSharers.append(character)
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
                        print("Subbing " + subCharacter + " for " + person + " (years: " + ageShared + " (" + ageType + ")" + ")")
                        reasonSubbing[person] = ["Ages", ageShared + " (" + ageType + ")"]
                        charactersReplacement[person] = subCharacter
                        escapeCharacter = ":)"
                        replacedViaTags.append(person)
                    else:
                        print("Ages were an ultimate failure.")
                if RNGRandomSwapper > 98:
                    print(person + " stays the same")

                    charactersReplacement[person] = person
                    print("Not subbing " + charactersReplacement[person] + " for " + person + " (no change)")
                    reasonSubbing[person] = ["No Change", ""]
                    escapeCharacter = ":)"
                    replacedViaTags.append(person)
    
    #print("\nFinal Generation: ")
    #for person in charactersReplacement.keys():
        #print(person + " was substituted with " + charactersReplacement[person] + " via " + reasonSubbing[person][0] + " (" + reasonSubbing[person][1] + ")")                     
    for character in charactersReplacement.keys():
        otherAddedCharacters.append(character)
    for character in charactersReplacement.values():
        otherAddedCharacters.append(character)
    print("Completed Generation!")
    return [charactersReplacement, reasonSubbing, otherAddedCharacters]