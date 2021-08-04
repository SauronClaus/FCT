alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

searchColor = ""

lowPop = []
mediumPop = []
highPop = []

pops = {
    "Low":lowPop,
    "Medium":mediumPop,
    "High":highPop
}

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                #print(entry + ": " + str(len(characterInfo)))
                try:
                    characterPop = characterInfo[17]
                    if characterPop == searchColor:
                        print(entry)
                    pops[characterPop].append(characterInfo[0])
                except:
                    print(entry + " is broken!")
                
popFile = open("popularity.txt","w")
total = len(lowPop) + len(mediumPop) + len(highPop)
lowPopString = "Low (" + str(len(lowPop)) + "/" + str(total) + "): "
for character in lowPop:
    lowPopString = lowPopString + character + ", "
lowPopString = lowPopString[0:len(lowPopString)-2:]

mediumPopString = "Medium (" + str(len(mediumPop)) + "/" + str(total) + "): "
for character in mediumPop:
    mediumPopString = mediumPopString + character + ", "
mediumPopString = mediumPopString[0:len(mediumPopString)-2:]

highPopString = "High (" + str(len(highPop)) + "/" + str(total) + "): "
for character in highPop:
    highPopString = highPopString + character + ", "
highPopString = highPopString[0:len(highPopString)-2:]

popFile.write(lowPopString + "\n")
popFile.write(mediumPopString + "\n")
popFile.write(highPopString)

print("Completed!")