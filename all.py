# Has a few methods to make full definitions of all of a certain type.

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import os
def allGroups():
    groupsLarge = {}
    # It's a dict of string/list pairs.

    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 24 or len(characterInfo) == 29:
                    groups = characterInfo[18].split(",")
                    for group in groups:
                        if group != "":
                            try:
                                groupsLarge[group].append(entry[0:len(entry)-4:])
                            except:
                                groupsLarge[group] = []
                                groupsLarge[group].append(entry[0:len(entry)-4:])
    return groupsLarge
# Returns a dict of string/list pairs; the string is the group name, the list is the people in the group.

def allPeople():
    characters = {}
    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                fileName = entry[0:len(entry)-4:]

                if len(characterInfo) == 29 or len(characterInfo) == 24:
                    characters[fileName] = characterInfo
    return characters
# Returns a dict of people, with the pair being filename/character info list

def allFranchises():
    franchises = {}

    for letter in alphabet:
            basepath = 'Franchises/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    #print(entry)
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read().split("\n")
                    if len(franchiseInfo) == 17:
                        franchises[entry[0:len(entry)-4:]] = franchiseInfo

# Returns a dict of franchises, with the pair being filename/franchise info list