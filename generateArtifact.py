import encodings
import random
import os
from re import A

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

powerLevelsDict = {"Mundane": 0, "Slightly-Magical": 1, "City": 2, "Country": 3, "World": 4, "Cosmic": 5, "Interuniversal": 6, "Omnipotent": 7}
additionalPowerLevels = {4: "Tier 1", 3: "Tier 2", 2: "Tier 3", 1: "Tier 4"}

def generateArtifact(artifactOrig, guildID, ):
    artifactInfoOrigFile = open("Artifacts\\" + artifactOrig + ".txt", "r", encoding='utf8')
    artifactOrigInfo = artifactInfoOrigFile.read().split("\n")
    print("Subbing " + artifactOrigInfo[0])
    artifactSub = ""

    reasonForSubbing = []
    while artifactSub == "":
        artifactListFull = {}
        basepath = "Artifacts"
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                if entry != "readMe.txt":
                    artifactFile = open(basepath + "\\" + entry, "r", encoding='utf8')
                    artifactInfo = artifactFile.read().split("\n")
                    if len(artifactInfo) == 16:
                        artifactListFull[entry[0:len(entry)-4:]] = artifactInfo
        RNG = random.randint(1, 100)
        if RNG <= 40:
            artifactSub = artifactOrig
            reasonForSubbing = ["No Change", "No Change"]
        if RNG > 40 and RNG <= 55:
            # Tags
        if RNG > 55 and RNG <= 60:
            # Full random
        if RNG > 70 and RNG <= 80:
            # Wielders
        if RNG > 80 and RNG <= 90:
            mediumsList = artifactOrigInfo[8].split(",")
            genList = []
            for artifactName in artifactListFull:
                artifactMediums = artifactListFull[artifactName][8].split(",")
                for medium in artifactMediums:
                    if medium in mediumsList:
                        artifactRarity = artifactListFull[artifactName][8]
                        result = chooseArtifact(genList, )
        

        if RNG > 90 and RNG <= 100:
            #Types
       



generateArtifact("Mjolnir")