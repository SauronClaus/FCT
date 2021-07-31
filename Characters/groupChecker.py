# Prints out the people in the group in "Group Name"

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

groupName = "Super Smash Bros"
groupMembers = []
import os

groupsLarge = {}

print("Start!")
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            #print(characterInfo.split("\n")[0])
            if len(characterInfo) == 24:
                groups = characterInfo[18].split(",")
                for group in groups:
                    if group != "":
                        if groupName in group:
                            print(entry)
                        try:
                            groupsLarge[group].append(entry[0:len(entry)-4:])
                        except:
                            groupsLarge[group] = []
                            groupsLarge[group].append(entry[0:len(entry)-4:])

tiedGroupsInOrder = {}
tiedGroupsFile = open("Characters\\tiedGroups.txt","r",encoding="utf8")
tiedGroups = tiedGroupsFile.read().split("\n")
for tiedGroup in tiedGroups:
    if tiedGroup != "":
        for group in tiedGroup.split(";")[1].split(","):
            if group in groupsLarge.keys():
                tiedGroupsInOrder[group] = groupsLarge[group]
                del groupsLarge[group]
writeFile = open("Characters\\groups.txt", "w", encoding='utf8')
for group in tiedGroupsInOrder.keys():
    print(group + " (" + str(len(tiedGroupsInOrder[group]))+ ")")
    groupString = group + ": "
    for person in tiedGroupsInOrder[group]:
        groupString = groupString + person + ", "
    groupString = groupString[0:len(groupString)-2:]
    writeFile.write(groupString + "\n")
    
print("-----------------------------------------------------------------")
writeFile.write("\n")

for group in groupsLarge.keys():
    print(group + " (" + str(len(groupsLarge[group]))+ ")")
    groupString = group + ": "
    for person in groupsLarge[group]:
        groupString = groupString + person + ", "
    groupString = groupString[0:len(groupString)-2:]
    writeFile.write(groupString + "\n")
writeFile.close()
