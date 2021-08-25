for minions in completedMinions:
    minionsFile = open("Minions\\" + minions + ".txt", "r", encoding='utf8')
    minionsInfo = minionsFile.read().split("\n")
    minionPowers = minionsInfo[24].split(",")
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
    powerSet = powerSet + "\t-All " + " (" + str(len(powerDict[powerName]["Total"])) + "/" + str(len(completedCharacters)) + "): "
    for person in powerDict[powerName]["Total"]:
        powerSet = powerSet + person + ", "
    powerSet = powerSet[0:len(powerSet)-2:] + "\n"
    powerString = powerString + "\n" + powerSet
       
powersFile.write(powerString)