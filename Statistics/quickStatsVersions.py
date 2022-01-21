# This program fills out all of the files under Statistics\\Versions

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os
def quickStatsVersions():
    completedVersions = []
    weirdVersions = []
    allVersions = {}

    highRarity = []
    mediumRarity = []
    lowRarity = []
    veryLowSpecialRarity = []
    
    # List all files in a directory using os.listdir
    for letter in alphabet:
        basepath = 'Versions\\' + letter
        for folder in os.listdir(basepath):
            for entry in os.listdir(basepath + "\\" + folder):
                #print(basepath + "\\" + folder + "\\" + entry)
                if os.path.isfile(basepath + "\\" + folder + "\\" + entry):
                    versionFile = open(basepath + "\\" + folder + "\\" + entry, "r", encoding='utf8')
                    versionInfo = versionFile.read().split("\n")
                    if len(versionInfo) == 2:
                        completedVersions.append(entry[0:len(entry)-4:])
                        if versionInfo[1] == "High":
                            highRarity.append(entry[0:len(entry)-4:])
                        if versionInfo[1] == "Medium":
                            mediumRarity.append(entry[0:len(entry)-4:])
                        if versionInfo[1] == "Low":
                            lowRarity.append(entry[0:len(entry)-4:])
                        if versionInfo[1] == "Very Low*":
                            veryLowSpecialRarity.append(entry[0:len(entry)-4:])
                        #print("Complete: " + entry[0:len(entry)-4:])

                    else:
                        weirdVersions.append(entry[0:len(entry)-4:])
                        #print("Weird: " + entry[0:len(entry)-4:])
                    allVersions[entry[0:len(entry)-4:]] = folder

                    
    
    statsFile = open("Statistics\\Versions\\stats.txt", "w",encoding='utf8')

    quickStatNum = str(len(completedVersions)) + " (completed)/" + str(len(weirdVersions)) + " (weird)/Total:" + str(len(allVersions.keys()))

    rarities = {
        "High": len(highRarity),
        "Medium": len(mediumRarity),
        "Low": len(lowRarity),
        "Very Low*": len(veryLowSpecialRarity)
    }

    readFile = open("Statistics\\Versions\\rarities.txt", "w",encoding='utf8')
    sortedDict = sorted(rarities, key=rarities.get, reverse=True)
    for entry in sortedDict:
        print(str(entry) + ": " + str(rarities[entry]))
        assemble = str(entry) + " (" + str(rarities[entry]) + "):"
        writeArray = []
        if entry == "High":
            writeArray = highRarity
        if entry == "Medium":
            writeArray = mediumRarity
        if entry == "Low":
            writeArray = lowRarity
        if entry == "Very Low*":
            writeArray = veryLowSpecialRarity

        for version in writeArray:
            assemble = assemble + " " + version + " (" + allVersions[version] + ")" + ","
        readFile.write(assemble[0:len(assemble)-1:] + "\n")
    

    print(quickStatNum)

    statsFile.write(quickStatNum)

    statsFile.close()
    readFile.close()
    print("Completed Versions Updates!")

quickStatsVersions()