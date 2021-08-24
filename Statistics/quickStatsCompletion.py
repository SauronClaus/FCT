# This file fills out the file labled "completion rankings.txt" along with serving as a spring board for the three methods imported.

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
import os

from quickStatsArtifacts import quickStatsArtifacts
from quickStatsCharacters import quickStatsCharacters
from quickStatsFranchises import quickStatsFranchise

def quickStatsCompletion():
    completedCharacters = []
    undoneCharacters = []
    needToUpdateCharacters = []
    weirdCharacters = []
    allCharacters = []
    newCharacterRankings = []

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
                    else:
                        newCharacterRankings.append(entry[0:len(entry)-4:])
                else:
                    if len(characterInfo) == 5:
                        undoneCharacters.append(entry[0:len(entry)-4:])
                    else:
                        if len(characterInfo) == 17 or len(characterInfo) == 22 or len(characterInfo) == 24:
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

    weirdFile = open("Statistics\\Completetion Rankings\\People\\weirdCharacters.txt", "w", encoding='utf8')
    updateFile = open("Statistics\\Completetion Rankings\\People\\needToUpdateCharacters.txt", "w", encoding='utf8')
    incompleteFile = open("Statistics\\Completetion Rankings\\People\\incompleteCharacters.txt", "w", encoding='utf8')
    completeFile = open("Statistics\\Completetion Rankings\\People\\completedCharacters.txt", "w", encoding='utf8')
    newCharacterRankingsFile = open("Statistics\\Completetion Rankings\\People\\newUpdate.txt", "w", encoding='utf8')
    for character in completedCharacters:
        completeFile.write(character + "\n")

    for character in undoneCharacters:
        incompleteFile.write(character + "\n")
    for character in needToUpdateCharacters:
        updateFile.write(character + "\n")
    for character in weirdCharacters:
        weirdFile.write(character + "\n")

    weirdFile.close()
    updateFile.close()
    incompleteFile.close()
    completeFile.close()


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
                if len(franchiseInfo) == 18:
                    completedFranchises.append(entry[0:len(entry)-4:])
                else:
                    if len(franchiseInfo) == 7 or len(franchiseInfo) == 17:
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
                if len(ArtifactsInfo) == 14:
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

    completionFile = open("Statistics\\Completetion Rankings\\completion rankings.txt", "w", encoding='utf8')
    completionFile.write("Characters (" + str(round(len(completedCharacters)/len(allCharacters),4)*100) + "%):\n   -" + str(len(completedCharacters)) + " completed characters.\n   -" + str(len(undoneCharacters)) + " incomplete characters.\n   -" + str(len(needToUpdateCharacters)) + " unupdated characters.\n   -" + str(len(weirdCharacters)) + " weird characters.\n   -" + str(len(allCharacters)) + " total characters.\n")
    completionFile.write("Franchises: (" + str(round(len(completedFranchises)/len(allFranchises),4)*100) + "%):\n   -" + str(len(completedFranchises)) + " completed franchises.\n   -" + str(len(undoneFranchises)) + " incomplete franchises.\n   -" + str(len(needToUpdateFranchises)) + " unupdated franchises\n   -" + str(len(weirdFranchises)) + " weird franchises.\n   -" + str(len(allFranchises)) + " total franchises.\n")
    completionFile.write("Artifacts: (" + str(round(len(completedArtifacts)/len(allArtifacts),4)*100) + "%):\n   -" + str(len(completedArtifacts)) + " completed artifacts.\n   -" + str(len(undoneArtifacts)) + " incomplete artifacts.\n   -" + str(len(needToUpdateArtifacts)) + " unupdated artifacts.\n   -" + str(len(weirdArtifacts)) + " weird artifacts.\n   -" + str(len(allArtifacts)) + " total artifacts.\n")
    completionFile.write("Adjectives: (" + str(round(len(completedAdjectives)/len(allAdjectives),4)*100) + "%):\n   -" + str(len(completedAdjectives)) + " completed adjectives.\n   -" + str(len(undoneAdjectives)) + " incomplete adjectives.\n   -" + str(len(needToUpdateAdjectives)) + " unupdated adjectives.\n   -" + str(len(weirdAdjectives)) + " weird adjectives.\n   -" + str(len(allAdjectives)) + " total adjectives.")

    print("Completed Completion Update!")

print("Begin update quick stats!")
quickStatsArtifacts()
quickStatsCharacters()
quickStatsFranchise()
quickStatsCompletion()
print("Completed all!")