# This program fills out all of the files under Statistics\\Characters

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os
powerDict = {}
powersFile = open("Statistics\\powers.txt", "w",encoding='utf8')
completedCharacters = []
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            

            if len(characterInfo) == 29:
                if characterInfo[24] != "":
                    completedCharacters.append(entry[0:len(entry)-4:])
                    characterPowers = characterInfo[24].split(",")
                    for powerSetFull in characterPowers:
                        #print(entry[0:len(entry)-4:] + ": " + powerSetFull)
                        powerSet = powerSetFull.split("|")
                        characterPower = powerSet[0]
                        characterPowerCategory = powerSet[1]
                        character = entry[0:len(entry)-4:] + " (Tier " + powerSet[2] + ")"
                        try:
                            powerDict[characterPower][characterPowerCategory].append(character)
                            powerDict[characterPower]["Total"].append(character)
                        except:
                            #print("Stage 1 failure (location: " + character + ")")
                            try:
                                powerDict[characterPower][characterPowerCategory] = [character]
                                powerDict[characterPower]["Total"].append(character)
                            except:
                                #print("Stage 2 failure (location: " + character + ")")
                                try:
                                    powerDict[characterPower] = {characterPowerCategory: [character],"Total":[character]}
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
print("Completed!")