# Updates the characters in the bot to a new line format. 

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            characterFile.close()
            if len(characterInfo) == 29:
                characterFile = open(basepath + "/" + entry, "w", encoding='utf8')
                x = 1
                for info in characterInfo:
                    if x < 27:
                        characterFile.write(info + "\n")
                        x+=1
                if characterInfo[27] == "":
                    characterFile.write("Sebastian\n\nNo")
                else:
                    characterFile.write("Sebastian\n" + characterInfo[27] + "\nNo")


print("Completed!")