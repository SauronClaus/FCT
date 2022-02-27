# Handles person generation for the matches. Moved to a seperate file because it's big as heck.
import random
import os
from all import allFranchises
from all import allGroups
from all import allPeople
from generateAllPeople import genAllPeople
from generateAllPeople import genMinions

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate(guildID):
    franchises = []

    for letter in alphabet:
            basepath = 'Franchises/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    #print(entry)
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read().split("\n")
                    if len(franchiseInfo) == 19:
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
    
    additives = {}
    peopleReplacementOrigs = franchiseInfo[7].split("|") #The original list of people that comes straight from the franchise file.
    for person in peopleReplacementOrigs:
        bing = person.split(";")
        if len(bing) > 1:
            index = peopleReplacementOrigs.index(person)
            personName = bing[0]
            restriction = bing[1]
            peopleReplacementOrigs[index] = personName
            additives[personName] = restriction

    antagonistReplacementOrigs = franchiseInfo[8].split("|") #The original list of antagonists that comes straight from the franchise file.
    for person in antagonistReplacementOrigs:
        bing = person.split(";")
        if len(bing) > 1:
            print(str(antagonistReplacementOrigs))
            index = antagonistReplacementOrigs.index(person)
            personName = bing[0]
            restriction = bing[1]
            antagonistReplacementOrigs[index] = personName
            additives[personName] = restriction
    artifactReplacementOrigs = franchiseInfo[10].split("|") #The original list of artifacts that comes straight from the franchise file.
    

    franchiseGroups = allGroups() #a dict of string/list pairs; the string is the group name, the list is the people in the group.
    people = allPeople()    
    otherAddedCharacters = []
    listen = genAllPeople(guildID, peopleReplacementOrigs, franchiseInfo, otherAddedCharacters, False)
    charactersReplacement = listen[0]
    charactersReasonSubbing = listen[1]
    otherAddedCharacters = listen[2]
    protagAdjectives = listen[3]
    version = listen[4]


    listenAntag = []
    if len(antagonistReplacementOrigs) > 1 or antagonistReplacementOrigs[0] != "":
        print("Antag Replace Orig: " + str(antagonistReplacementOrigs) + "/" + str(len(antagonistReplacementOrigs)))
        listenAntag = genAllPeople(guildID, antagonistReplacementOrigs, franchiseInfo, otherAddedCharacters, True)
        antagReplacement = listenAntag[0]
        antagReasonSubbing = listenAntag[1]
        otherAddedCharacters = listenAntag[2]
        antagAdjectives = listenAntag[3]
        antagVersion = listenAntag[4]
    artifactReplacement = {}

    print("\nFinal Generation Protagonists: ")
    for person in charactersReplacement.keys():
        try:
            print(person + " was substituted with " + charactersReplacement[person] + " (" + version[charactersReplacement[person]] + ") via " + charactersReasonSubbing[person][0] + " (" + charactersReasonSubbing[person][1] + ")")                     
        except:
            print(person + " was substituted with " + charactersReplacement[person] + " via " + charactersReasonSubbing[person][0] + " (" + charactersReasonSubbing[person][1] + ")")                     
    if len(antagonistReplacementOrigs) > 1 or antagonistReplacementOrigs[0] != "":
        print("\nFinal Generation Antagonists: ")
        for person in antagReplacement.keys():
            try:
                print(person + " was substituted with " + antagReplacement[person] + " (" + antagVersion[antagReplacement[person]] + ") via " + antagReasonSubbing[person][0] + " (" + antagReasonSubbing[person][1] + ")")                     
            except:
                print(person + " was substituted with " + antagReplacement[person] + " via " + antagReasonSubbing[person][0] + " (" + antagReasonSubbing[person][1] + ")")                     
    info = []
    if franchiseInfo[9] != "":
        info = genMinions(franchiseName, franchiseInfo, guildID)

    if len(info) > 1:
        print("\nFinal Generation Minions: ")
        for minion in info[0].keys():
            if len(info[1][minion]) > 1:
                print(minion + " was substituted with " + info[0][minion] + " via " + info[1][minion][0] + " (" + info[1][minion][1] + ")")
            else:
                print(minion + " was substituted with " + info[0][minion] + " via " + info[1][minion][0])


    
    return[listen, listenAntag, [franchiseName,franchiseInfo], info, additives]

    # These are the heavy ones. These are always active, and serve to stick in the people when need be. 