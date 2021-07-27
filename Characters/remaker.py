alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            characterFile.close()
            if len(characterInfo) != 17 and len(characterInfo) != 22:
                newFile = open(basepath + "/" + entry, "w", encoding='utf8')
                if len(characterInfo) == 3 or len(characterInfo) == 5:
                    print(characterInfo[0] + " (!)")
                    newFile.write(characterInfo[0] + "\n" + characterInfo[1] + "\n\n\n" + characterInfo[2])
                if len(characterInfo) == 16:
                    print(characterInfo[0] + " (*)")
                    newFile.write(characterInfo[0] + "\n" + characterInfo[1] + "\n\n\n" + characterInfo[2] + "\n" + characterInfo[3] + "\n" + characterInfo[4] + "\n" + characterInfo[5] + "\n" + characterInfo[6] + "\n" + characterInfo[7] + "\n" + characterInfo[8] + "\n" + characterInfo[9] + "\n" + characterInfo[10] + "\n" + characterInfo[11] + "\n" + characterInfo[13] + "\n" + characterInfo[14] + "\n" + characterInfo[15])
                if len(characterInfo) == 0 or len(characterInfo) == 1:
                    print(characterInfo[0] + "/" + entry + " (?)")
                newFile.close()
print("Completed!")

