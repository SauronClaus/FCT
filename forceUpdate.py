# Updates the characters in the bot to a new line format. 

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

for letter in alphabet:
    basepath = 'Franchises/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            characterFile.close()
            if len(characterInfo) == 18:
                characterFile = open(basepath + "/" + entry, "a", encoding='utf8')
                characterFile.write("\nSebastian")


print("Completed!")