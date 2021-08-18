
def chooseCharacter(subCharacter, subPowerLevel, currentPowerLevel, subRarity, swapList):
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