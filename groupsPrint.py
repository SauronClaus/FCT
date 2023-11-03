alphabet = ["#", "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import os


otherInfo= {}
groups = []
for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 30:
                    for group in characterInfo[18].split(","):
                        if not(group in groups):
                            groups.append(group)
                            otherInfo[group] = [group, characterInfo[1], "\n", "\n", "\n", "\n", [entry[0:len(entry)-4:]], "\n", "\n", "\n", "\n", characterInfo[16], characterInfo[17], characterInfo[20], "\n", characterInfo[21], characterInfo[25], "Sebastian", characterInfo[29]]
                        else:
                            otherInfo[group][6].append(entry[0:len(entry)-4:])
                            if characterInfo[29] != "No":
                                otherInfo[group][18] == characterInfo[29]

for group in groups:
    firstLetter = group[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    try:
        groupFile = open("Groups\\" + firstLetter + "\\" + group + ".txt", "r", encoding='utf8')
    except:
        try:
            groupFile = open("Groups\\" + firstLetter + "\\" + group + ".txt", "w", encoding='utf8')
            groupString = ""
            info = otherInfo[group]
            memberString = ""
            #print("info: " + str(info))
            for groupMember in info[6]:
                memberString = memberString + groupMember + ","
            memberString = memberString[0:len(memberString)-1:]
            if "Permutations" in info[0]:
                groupString = info[0] + "\n" + info[1] + "\nVarious permutations across the multiverse of " + info[0][0:len(info[0])-15:] + ".\nNone\nNone\n" + info[0][0:len(info[0])-15:] + "\n" + memberString + "\n18|1\nPermutations\n10. Gender- is this group all male? All female? Neither?\nPermutations,IRL People\n" + info[11] + "\n" + info[12] + "\n" + info[13] + "\nWhite\n" + info[15] + "\n" + info[16] + "\nSebastian\n" + info[18]
            else:
                groupString = info[0] + "\n" + info[1] + "\n3. A description of the group.\n4. An image of the group.\n5. An article with more info about the group.\n6. Aliases for the group (if applicable)\n" + memberString + "\n8. Age of the group- how long has it been around for?\n9. Type of group- \n10. Gender- is this group all male? All female? Neither?\n11. Tags!\n" + info[11] + "\n" + info[12] + "\n" + info[13] + "\n15. Color\n" + info[15] + "\n" + info[16] + "\nSebastian\n" + info[18]
            groupFile.write(groupString)
            groupFile.close()
        except:
            print(str(group) + " [" + str(otherInfo[group][6]) + "]")

print("Completed!")