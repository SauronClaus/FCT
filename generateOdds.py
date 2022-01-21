# Generates the odds for someone to be chosen. Moved to a seperate program file so I can mess with the 
# odds a bit easier.
import random

from all import allPeople
def chooseCharacter(guildID, people, subMedium, subCharacter, subPowerLevel, currentPowerLevel, subRarity, swapList):
    specialConditions = ""
    if subMedium == False and len(people[subCharacter]) == 30:
        specialConditions = people[subCharacter][29]
    if specialConditions == "No Sub In":
            print("Invalid Substitution: " + subCharacter + " (No Sub In)")
    else:
        specialConditionsTest = specialConditions.split("|")
        if len(specialConditionsTest) > 1:
            print("len special condtions = " + str(len(specialConditionsTest)))
            if specialConditionsTest[0] == "Guild Only":
                if int(specialConditionsTest[1]) != guildID and guildID != 620964009247768586:
                    print("Couldn't sub " + subCharacter + " (Invalid guild; guilds did not match)")
        else:
            if subPowerLevel < currentPowerLevel and currentPowerLevel-subPowerLevel > 1:
                if subRarity == "Very Low":
                    RNG = random.randint(1,2)
                    if RNG == 1:
                        swapList.append(subCharacter)
                if subRarity == "Very Low*":
                    RNG = random.randint(1,100)
                    if RNG == 13:
                        print(">>>>>>>>>>>>>>>EVIL HARRISON PICKED<<<<<<<<<<<<<<<")
                        for x in range(100):
                            swapList.append(subCharacter)
                if subRarity == "Low":
                    swapList.append(subCharacter)
                if subRarity == "Medium":
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                if subRarity == "High":
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
            else:
                #print("Found Rarity: " + subRarity)
                if subRarity == "Very Low":
                    RNG = random.randint(1,2)
                    if RNG == 1:
                        swapList.append(subCharacter)
                        swapList.append(subCharacter)
                if subRarity == "Very Low*":
                    RNG = random.randint(1,100)
                    if RNG == 13:
                        print(">>>>>>>>>>>>>>>EVIL HARRISON PICKED<<<<<<<<<<<<<<<")
                        for x in range(100):
                            swapList.append(subCharacter)
                if subRarity == "Low":
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                if subRarity == "Medium":
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                if subRarity == "High":
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
                    swapList.append(subCharacter)
    return swapList

def chooseVersion(subVersions):
    swapList = []
    for subCharacter in subVersions.keys():
        subRarity = subVersions[subCharacter]
        print("Rarity! ~" + subRarity + "~")
        if subRarity == "Very Low":
            RNG = random.randint(1,2)
            if RNG == 1:
                swapList.append(subCharacter)
                swapList.append(subCharacter)
            if subRarity == "Very Low*":
                RNG = random.randint(1,100)
                if RNG == 13:
                    print(">>>>>>>>>>>>>>>VERY RARE VERSION PICKED<<<<<<<<<<<<<<<")
                    for x in range(100):
                        swapList.append(subCharacter)
        if subRarity == "Low":
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            print("Added " + subCharacter)
        if subRarity == "Medium":
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            print("Added " + subCharacter)

        if subRarity == "High":
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            swapList.append(subCharacter)
            print("Added " + subCharacter)

    print(str(0) + "/" + str(len(swapList)-1))
    RNG = random.randint(0,len(swapList)-1)
    version = swapList[RNG]
    print(version + " chosen!")
    return version