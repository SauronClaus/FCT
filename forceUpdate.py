# Updates the characters in the bot to a new line format. 

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

for letter in alphabet:
    basepath = 'Characters\\' + letter + "\\"
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read()
            characterFile.close()
            if len(characterInfo.split("\n")) == 29:
                characterFile = open(basepath + "/" + entry, "w", encoding='utf8')
                for line in characterInfo.split("\n"):
                    if characterInfo.split("\n").index(line) != 28:
                        characterFile.write(line + "\n")
                characterFile.write("\n")
                characterFile.write(characterInfo.split("\n")[28])
                characterFile.close()

print("Completed!")