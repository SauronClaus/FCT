alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

artifactList = []
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 22:
                #print(entry + ": " + str(len(characterInfo)))
                characterWeapon = characterInfo[21]
                if characterWeapon != "":
                    print(entry[0:len(entry)-4:] + ": " + characterWeapon)
                    try:
                        weaponFile = open("Artifacts\\" + characterWeapon + ".txt", "r")
                    except:
                        weaponFile = open("Artifacts\\" + characterWeapon + ".txt", "w")
                        weaponFile.write(characterWeapon + "\n")

