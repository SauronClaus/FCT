# Handles person generation for the matches. Moved to a seperate file because it's big as heck.
import random
import os
from all import allFranchises
from all import allGroups
from all import allPeople
from generateAllPeople import genAllPeople

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate():
    franchises = []

    for letter in alphabet:
            basepath = 'Franchises/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    #print(entry)
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read().split("\n")
                    if len(franchiseInfo) == 17:
                        franchises.append(entry[0:len(entry)-4:])
                        if franchiseInfo[15] == "Medium" or franchiseInfo[15] == "High":
                            franchises.append(entry[0:len(entry)-4:])
                        if franchiseInfo[15] == "High":
                            franchises.append(entry[0:len(entry)-4:])
                        


    print("Franchise generation completed.")

    RNG = random.randint(0,len(franchises)-1)
    print("Chose " + franchises[RNG] + " (" + str(RNG) + "/" + str(len(franchises)) + ")")
    franchiseName = franchises[RNG]

    firstChar = franchiseName[0:1:]
    if firstChar in numbers:
        firstChar = "#"
    print("Opening path to " + franchiseName + ": Franchises\\" + firstChar + "\\" + franchiseName + ".txt")
    print("\n")

    franchiseFile = open("Franchises\\" + firstChar + "\\" + franchiseName + ".txt", "r", encoding='utf8')
    franchiseInfo = franchiseFile.read().split("\n")

    peopleReplacementOrigs = franchiseInfo[7].split("|") #The original list of people that comes straight from the franchise file.
    antagonistReplacementOrigs = franchiseInfo[8].split("|") #The original list of antagonists that comes straight from the franchise file.
    artifactReplacementOrigs = franchiseInfo[9].split("|") #The original list of artifacts that comes straight from the franchise file.
    

    franchiseGroups = allGroups() #a dict of string/list pairs; the string is the group name, the list is the people in the group.
    people = allPeople()    
    otherAddedCharacters = []
    listen = genAllPeople(peopleReplacementOrigs, franchiseInfo, otherAddedCharacters, False)
    charactersReplacement = listen[0]
    charactersReasonSubbing = listen[1]
    otherAddedCharacters = listen[2]
    protagAdjectives = listen[3]


    listenAntag = []
    if len(antagonistReplacementOrigs) > 1 or antagonistReplacementOrigs[0] != "":
        print("Antag Replace Orig: " + str(antagonistReplacementOrigs) + "/" + str(len(antagonistReplacementOrigs)))
        listenAntag = genAllPeople(antagonistReplacementOrigs, franchiseInfo, otherAddedCharacters, True)
        antagReplacement = listenAntag[0]
        antagReasonSubbing = listenAntag[1]
        otherAddedCharacters = listenAntag[2]
        antagAdjectives = listenAntag[3]
    artifactReplacement = {}

    print("\nFinal Generation Protagonists: ")
    for person in charactersReplacement.keys():
        print(person + " was substituted with " + charactersReplacement[person] + " via " + charactersReasonSubbing[person][0] + " (" + charactersReasonSubbing[person][1] + ")")                     
    if len(antagonistReplacementOrigs) > 1 or antagonistReplacementOrigs[0] != "":
        print("\nFinal Generation Antagonists: ")
        for person in antagReplacement.keys():
            print(person + " was substituted with " + antagReplacement[person] + " via " + antagReasonSubbing[person][0] + " (" + antagReasonSubbing[person][1] + ")")                     

    return[listen, listenAntag, [franchiseName,franchiseInfo]]
    # These are the heavy ones. These are always active, and serve to stick in the people when need be. 