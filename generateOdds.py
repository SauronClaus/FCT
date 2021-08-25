# Generates the odds for someone to be chosen. Moved to a seperate program file so I can mess with the 
# odds a bit easier.

from all import allPeople
def chooseCharacter(subCharacter, subPowerLevel, currentPowerLevel, subRarity, swapList):
    people = allPeople()
    specialConditions = people[subCharacter][28]
    if specialConditions == "No Sub In":
        print("Invalid Substitution: " + subCharacter + " (No Sub In)")
    else:
        if subPowerLevel < currentPowerLevel and currentPowerLevel-subPowerLevel > 1:
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