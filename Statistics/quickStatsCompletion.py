# This file fills out the file labled "completion rankings.txt" along with serving as a spring board for the five methods imported.

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

from quickStatsArtifacts import quickStatsArtifacts
from quickStatsCharacters import quickStatsCharacters
from quickStatsFranchises import quickStatsFranchise
from quickStatsMinions import quickStatsMinions
from quickStatsVersions import quickStatsVersions

def quickStatsCompletion():
    completedCharacters = []
    undoneCharacters = []
    needToUpdateCharacters = []
    weirdCharacters = []
    allCharacters = []
    newCharacterRankings = []
    noSubCharacters = []
    guildLockedCharacters = []
    regularRestict = []

    # List all files in a directory using os.listdir
    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 30:
                    completedCharacters.append(entry[0:len(entry)-4:])
                    if characterInfo[28] == "No":
                        regularRestict.append(entry[0:len(entry)-4:])
                    else:
                        if characterInfo[28] == "No Sub In":
                            noSubCharacters.append(entry[0:len(entry)-4:])
                        else:
                            if characterInfo[28].split("|")[0] == "Guild Only":
                                guildLockedCharacters.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 5:
                        undoneCharacters.append(entry[0:len(entry)-4:])
                    else:
                        if len(characterInfo) == 17 or len(characterInfo) == 22 or len(characterInfo) == 24 or len(characterInfo) == 29:
                            needToUpdateCharacters.append(entry[0:len(entry)-4:])
                        else:
                            weirdCharacters.append(entry[0:len(entry)-4:])
                allCharacters.append(entry[0:len(entry)-4:])
                #if characterInfo[0] != entry[0:len(entry)-4:]:
                    #print("Check " + characterInfo[0] + " (" + entry[0:len(entry)-4:] + ")")

    completedCharacters.sort()
    undoneCharacters.sort()
    needToUpdateCharacters.sort()
    weirdCharacters.sort()
    allCharacters.sort()
    newCharacterRankings.sort()
    noSubCharacters.sort()
    guildLockedCharacters.sort()
    regularRestict.sort()

    weirdFile = open("Statistics\\Completetion Rankings\\People\\weirdCharacters.txt", "w", encoding='utf8')
    updateFile = open("Statistics\\Completetion Rankings\\People\\needToUpdateCharacters.txt", "w", encoding='utf8')
    incompleteFile = open("Statistics\\Completetion Rankings\\People\\incompleteCharacters.txt", "w", encoding='utf8')
    completeFile = open("Statistics\\Completetion Rankings\\People\\completedCharacters.txt", "w", encoding='utf8')
    newCharacterRankingsFile = open("Statistics\\Completetion Rankings\\People\\newUpdate.txt", "w", encoding='utf8')
    guildLockFile = open("Statistics\\Completetion Rankings\\People\\guildLocked.txt", "w", encoding='utf8')
    noSubFile = open("Statistics\\Completetion Rankings\\People\\noSubstitute.txt", "w", encoding='utf8')
    regularRestictFile = open("Statistics\\Completetion Rankings\\People\\noRestrictions.txt", "w", encoding='utf8')


    for character in completedCharacters:
        completeFile.write(character + "\n")
    for character in undoneCharacters:
        incompleteFile.write(character + "\n")
    for character in needToUpdateCharacters:
        updateFile.write(character + "\n")
    for character in weirdCharacters:
        weirdFile.write(character + "\n")
    for character in guildLockedCharacters:
        guildLockFile.write(character + "\n")
    for character in noSubCharacters:
        noSubFile.write(character + "\n")
    for character in newCharacterRankings:
        newCharacterRankingsFile.write(character + "\n")
    for character in regularRestict:
        regularRestictFile.write(character + "\n")

    weirdFile.close()
    updateFile.close()
    incompleteFile.close()
    completeFile.close()
    guildLockFile.close()
    noSubFile.close()
    newCharacterRankingsFile.close()
    regularRestictFile.close()


    weirdFile = open("Statistics\\Completetion Rankings\\Franchises\\weirdFranchises.txt", "w", encoding='utf8')
    updateFile = open("Statistics\\Completetion Rankings\\Franchises\\needToUpdateFranchises.txt", "w", encoding='utf8')
    incompleteFile = open("Statistics\\Completetion Rankings\\Franchises\\incompleteFranchises.txt", "w", encoding='utf8')
    completeFile = open("Statistics\\Completetion Rankings\\Franchises\\completedFranchises.txt", "w", encoding='utf8')


    completedFranchises = []
    undoneFranchises = []
    needToUpdateFranchises = []
    weirdFranchises = []
    allFranchises = []

    for letter in alphabet:
        basepath = 'Franchises/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                franchiseInfo = franchiseFile.read().split("\n")
                if len(franchiseInfo) == 19:
                    completedFranchises.append(entry[0:len(entry)-4:])
                else:
                    if len(franchiseInfo) == 7 or len(franchiseInfo) == 17 or len(franchiseInfo) == 18:
                        needToUpdateFranchises.append(entry[0:len(entry)-4:])
                    else:
                        if len(franchiseInfo) == 2:
                            undoneFranchises.append(entry[0:len(entry)-4:])
                        else:
                            weirdFranchises.append(entry[0:len(entry)-4:])
                allFranchises.append(entry[0:len(entry)-4:])
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
    allArtifacts = []

    basepath = "Artifacts"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            ArtifactsFile = open(basepath + "/" + entry, "r", encoding='utf8')
            ArtifactsInfo = ArtifactsFile.read().split("\n")
            if entry != "readMe.txt":
                if len(ArtifactsInfo) == 16:
                    completedArtifacts.append(entry[0:len(entry)-4:])
                else:
                    if len(ArtifactsInfo) == 0:
                        needToUpdateArtifacts.append(entry[0:len(entry)-4:])
                    else:
                        if len(ArtifactsInfo) == 9:
                            undoneArtifacts.append(entry[0:len(entry)-4:])
                        else:
                            weirdArtifacts.append(entry[0:len(entry)-4:])
                allArtifacts.append(entry[0:len(entry)-4:])
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

    completedAdjectives = []
    undoneAdjectives = []
    needToUpdateAdjectives = []
    weirdAdjectives = []
    allAdjectives = []

    basepath = "Adjectives\\Descriptions"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            adjectiveInfo = open("Adjectives\\Descriptions\\" + entry, "r", encoding='utf8').read().split("\n")
            if (len(adjectiveInfo) == 1 and adjectiveInfo[0] != "") or len(adjectiveInfo) == 2:
                completedAdjectives.append(entry[0:len(entry)-4:])
            else:
                if len(adjectiveInfo) == 1 and adjectiveInfo[0] == "":
                    undoneAdjectives.append(entry[0:len(entry)-4:])
                else:
                    weirdAdjectives.append(entry[0:len(entry)-4:])
            allAdjectives.append(entry[0:len(entry)-4:])

    completedAdjectives.sort()
    undoneAdjectives.sort()
    needToUpdateAdjectives.sort()
    weirdAdjectives.sort()
    allAdjectives.sort()

    weirdFile = open("Statistics\\Completetion Rankings\\Minions\\weirdMinions.txt", "w", encoding='utf8')
    updateFile = open("Statistics\\Completetion Rankings\\Minions\\needToUpdateMinions.txt", "w", encoding='utf8')
    incompleteFile = open("Statistics\\Completetion Rankings\\Minions\\incompleteMinions.txt", "w", encoding='utf8')
    completeFile = open("Statistics\\Completetion Rankings\\Minions\\completedMinions.txt", "w", encoding='utf8')


    completedMinions = []
    undoneMinions = []
    needToUpdateMinions = []
    weirdMinions = []
    allMinions = []

    basepath = "Minions"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            MinionsFile = open(basepath + "/" + entry, "r", encoding='utf8')
            MinionsInfo = MinionsFile.read().split("\n")
            if entry != "readMe.txt":
                if len(MinionsInfo) == 24:
                    completedMinions.append(entry[0:len(entry)-4:])
                else:
                    if len(MinionsInfo) == 2:
                        needToUpdateMinions.append(entry[0:len(entry)-4:])
                    else:
                        if len(MinionsInfo) == 0:
                            undoneMinions.append(entry[0:len(entry)-4:])
                        else:
                            weirdMinions.append(entry[0:len(entry)-4:])
                allMinions.append(entry[0:len(entry)-4:])
    completedMinions.sort()
    undoneMinions.sort()
    needToUpdateMinions.sort()
    weirdMinions.sort()

    for minion in weirdMinions:
        weirdFile.write(minion + "\n")
    for minion in needToUpdateMinions:
        updateFile.write(minion + "\n")
    for minion in undoneMinions:
        incompleteFile.write(minion + "\n")
    for minion in completedMinions:
        completeFile.write(minion + "\n")

    weirdFile.close()
    updateFile.close()
    incompleteFile.close()
    completeFile.close()

    weirdFile = open("Statistics\\Completetion Rankings\\Versions\\weirdVersions.txt", "w", encoding='utf8')
    updateFile = open("Statistics\\Completetion Rankings\\Versions\\needToUpdateVersions.txt", "w", encoding='utf8')
    incompleteFile = open("Statistics\\Completetion Rankings\\Versions\\incompleteVersions.txt", "w", encoding='utf8')
    completeFile = open("Statistics\\Completetion Rankings\\Versions\\completedVersions.txt", "w", encoding='utf8')


    completedVersions = []
    undoneVersions = []
    needToUpdateVersions = []
    weirdVersions = []
    allVersions = []

    # List all files in a directory using os.listdir
    for letter in alphabet:
        basepath = 'Versions\\' + letter
        for folder in os.listdir(basepath):
            for entry in os.listdir(basepath + "\\" + folder):
                VersionsFile = open(basepath + "\\" + folder + "\\" + entry, "r", encoding='utf8')
                VersionsInfo = VersionsFile.read().split("\n")
                if len(VersionsInfo) == 2:
                    completedVersions.append(entry[0:len(entry)-4:])
                else:
                    weirdVersions.append(entry[0:len(entry)-4:])
                allVersions.append(entry[0:len(entry)-4:])
                VersionsFile.close()
    completedVersions.sort()
    undoneVersions.sort()
    needToUpdateVersions.sort()
    weirdVersions.sort()

    for version in weirdVersions:
        weirdFile.write(version + "\n")
    for version in needToUpdateVersions:
        updateFile.write(version + "\n")
    for version in undoneVersions:
        incompleteFile.write(version + "\n")
    for version in completedVersions:
        completeFile.write(version + "\n")

    weirdFile.close()
    updateFile.close()
    incompleteFile.close()
    completeFile.close()


    completionFile = open("Statistics\\Completetion Rankings\\completion rankings.txt", "w", encoding='utf8')
    completionFile.write("Characters (" + str(round((len(completedCharacters) + len(guildLockedCharacters) + len(noSubCharacters))/len(allCharacters),4)*100) + "%):\n   -" + str(len(completedCharacters)) + " completed characters.\n   -" + str(len(undoneCharacters)) + " incomplete characters.\n   -" + str(len(regularRestict)) + " characters with no restrictions.\n   -" + str(len(noSubCharacters)) + " unsubstitutable characters.\n   -" + str(len(guildLockedCharacters)) + " guild locked characters.\n   -" + str(len(needToUpdateCharacters)) + " unupdated characters.\n   -" + str(len(weirdCharacters)) + " weird characters.\n   -" + str(len(allCharacters)) + " total characters.\n")
    completionFile.write("Franchises: (" + str(round(len(completedFranchises)/len(allFranchises),4)*100) + "%):\n   -" + str(len(completedFranchises)) + " completed franchises.\n   -" + str(len(undoneFranchises)) + " incomplete franchises.\n   -" + str(len(needToUpdateFranchises)) + " unupdated franchises.\n   -" + str(len(weirdFranchises)) + " weird franchises.\n   -" + str(len(allFranchises)) + " total franchises.\n")
    completionFile.write("Artifacts: (" + str(round(len(completedArtifacts)/len(allArtifacts),4)*100) + "%):\n   -" + str(len(completedArtifacts)) + " completed artifacts.\n   -" + str(len(undoneArtifacts)) + " incomplete artifacts.\n   -" + str(len(needToUpdateArtifacts)) + " unupdated artifacts.\n   -" + str(len(weirdArtifacts)) + " weird artifacts.\n   -" + str(len(allArtifacts)) + " total artifacts.\n")
    completionFile.write("Adjectives: (" + str(round(len(completedAdjectives)/len(allAdjectives),4)*100) + "%):\n   -" + str(len(completedAdjectives)) + " completed adjectives.\n   -" + str(len(undoneAdjectives)) + " incomplete adjectives.\n   -" + str(len(needToUpdateAdjectives)) + " unupdated adjectives.\n   -" + str(len(weirdAdjectives)) + " weird adjectives.\n   -" + str(len(allAdjectives)) + " total adjectives.\n")
    completionFile.write("Minions: (" + str(round(len(completedMinions)/len(allMinions),4)*100) + "%):\n   -" + str(len(completedMinions)) + " completed minions.\n   -" + str(len(undoneMinions)) + " incomplete minions.\n   -" + str(len(needToUpdateMinions)) + " unupdated minions.\n   -" + str(len(weirdMinions)) + " weird minions.\n   -" + str(len(allMinions)) + " total minions.\n")
    completionFile.write("Variations: (" + str(round(len(completedVersions)/len(allVersions),4)*100) + "%):\n   -" + str(len(completedVersions)) + " completed versions.\n   -" + str(len(undoneVersions)) + " incomplete versions.\n   -" + str(len(needToUpdateVersions)) + " unupdated versions.\n   -" + str(len(weirdVersions)) + " weird versions.\n   -" + str(len(allVersions)) + " total versions.")

    print("Completed Completion Update!")

print("Begin update quick stats!")
quickStatsArtifacts()
quickStatsCharacters()
quickStatsFranchise()
quickStatsMinions()
quickStatsVersions()
quickStatsCompletion()
print("Completed all!")