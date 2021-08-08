import random
import os
from all import allFranchises
from all import allGroups
from all import allPeople


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
                        if franchiseInfo[14] == "Medium" or franchiseInfo[14] == "High":
                            franchises.append(entry[0:len(entry)-4:])
                        if franchiseInfo[14] == "High":
                            franchises.append(entry[0:len(entry)-4:])
                        


    print("Franchise generation completed.")

    RNG = random.randint(0,len(franchises)-1)
    print("Chose " + franchises[RNG] + " (" + str(RNG) + "/" + str(len(franchises)) + ")")
    franchiseName = franchises[RNG]

    firstChar = franchiseName[0:1:]
    if firstChar in numbers:
        firstChar = "#"
    print("Opening path to " + franchiseName + ": Franchises\\" + firstChar + "\\" + franchiseName + ".txt")
    
    franchiseFile = open("Franchises\\" + firstChar + "\\" + franchiseName + ".txt", "r", encoding='utf8')
    franchiseInfo = franchiseFile.read().split("\n")

    peopleReplacementOrigs = franchiseInfo[7].split("|")
    antagonistReplacementOrigs = franchiseInfo[8].split("|")
    artifactReplacementOrigs = franchiseInfo[9].split("|")
    
    # Requirements: 
    # - Every member of the group must be present inside the match
    franchiseGroups = allGroups()
    #a dict of string/list pairs; the string is the group name, the list is the people in the group.
    people = allPeople()
    groupsCanReplace = []
    # List of groups to replace (strings)
    endValidGroups = []

    for person in peopleReplacementOrigs:
        groupsPerson = people[person][18].split(",")
        for group in groupsPerson:
            if not(group in groupsCanReplace) and group != "":
                groupsCanReplace.append(group)
                #print("Added " + group)
                endValidGroups.append(group)
    
    for group in endValidGroups:
        #print("+" + group)
        for personGroupMember in franchiseGroups[group]:
            if not(personGroupMember in peopleReplacementOrigs) and group in groupsCanReplace:
                print("Removed " + group + " because of the exclusion of " + personGroupMember)
                #for foo in groupsCanReplace:
                    #print("<" + foo + ">/<" + group + ">")
                groupsCanReplace.remove(group)
            if len(franchiseGroups[group]) <= 1:
                print("Removed " + group + " because of the membership of only " + personGroupMember)
                #for foo in groupsCanReplace:
                    #print("<" + foo + ">/<" + group + ">")
                groupsCanReplace.remove(group)
      

    
    testString = ""
    for group in groupsCanReplace:
        #print("-" + group)
        testString = testString + group + ", "
    testString = testString[0:len(testString)-2:]
    print("For " + franchiseInfo[0] + ", " + str(len(groupsCanReplace)) + " groups were found in total. (" + testString + ")")
    
    #peopleReplacement = {}
    #for person in peopleReplacementOrigs:
        #peopleReplacement[person]
    

    antagonistReplacement = {}
    artifactReplacement = {}

    groupReplacementRNG = random.randint(1,4)
    groupReplacementRNG = 4
    validGroups = {}
    # This key is the group name (from groupsCanReplace) and the value is a list of the possible replacement groups
    if groupReplacementRNG == 4 and len(groupsCanReplace) > 0:
        for validGroup in groupsCanReplace:
            groups = {}
            for character in people.keys():
                characterInfo = people[character]
                if characterInfo[1] != franchiseInfo[11]:
                    for group in characterInfo[18].split(","):
                        if not(group in groupsCanReplace):
                            try:
                                groups[group] += 1
                            except:
                                groups[group] = 1
            for group in groups.keys():
                if groups[group] == len(franchiseGroups[validGroup]):
                    try:
                        validGroups[validGroup].append(group)
                    except:
                        validGroups[validGroup] = [group]
        for replaceGroup in validGroups.keys():
            testString = ""
            for group in validGroups[replaceGroup]:
                #print("-" + group)
                testString = testString + group + ", "
            testString = testString[0:len(testString)-2:]
            print(replaceGroup + ": " + testString)

            # Big things: weed out duplicate group members, remove groups without any valid matches.

                    
        

        
            

generate()