# Checks for any new artifacts, creates their file in Artifacts, and prints out a notice with the new ones.

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

import os

artifactList = []
newArtifacts = []

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 29:
                #print(entry + ": " + str(len(characterInfo)))
                characterWeapon = characterInfo[22]
                if characterWeapon != "":
                    for weapon in characterWeapon.split("|"):
                        print(entry[0:len(entry)-4:] + ": " + weapon)
                        try:
                            weaponFile = open("Artifacts\\" + weapon + ".txt", "r")
                        except:
                            weaponFile = open("Artifacts\\" + weapon + ".txt", "w")
                            weaponFile.write(weapon + "\n" + characterInfo[1] + "\n\n\n\n" + characterInfo[21] + "\n" + entry[0:len(entry)-4:] + "\n\n" + characterInfo[20])
                            newArtifacts.append(weapon)

for artifact in newArtifacts:
    print("New! " + artifact)
