import os

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if os.path.isdir("Versions") == False:
    os.makedirs("Versions")
    for letter in alphabet:
        os.makedirs("Versions\\" + letter)

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfoFull = characterFile.read()
            characterInfo = characterInfoFull.split("\n")
            if len(characterInfo) == 30:
                if characterInfo[27] != "":
                    if os.path.isdir("Versions\\" + letter + "\\" + entry[0:len(entry)-4:]) == False:
                        os.makedirs("Versions\\" + letter + "\\" + entry[0:len(entry)-4:])
                    characterWrite = open("Versions\\" + letter + "\\" + entry[0:len(entry)-4:] + "\\" + characterInfo[28] + ".txt", "w",encoding='utf8')
                    characterWrite.write(characterInfo[28] + "\n")
                    characterWrite.close()
                    for characterVersion in characterInfo[27].split(","):
                        characterWrite = open("Versions\\" + letter + "\\" + entry[0:len(entry)-4:] + "\\" + characterVersion + ".txt","w", encoding='utf8')
                        characterWrite.write(characterVersion + "\n")
                        characterWrite.close()
                else:
                    print(entry)
            characterFile.close()