alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
franchisesFull = {}
franchisesAllNoFill = {}
completedCharacters = []
import os

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read()
            if len(characterInfo.split("\n")) > 3:
                #print(entry[0:len(entry)-4:])
                franchise = characterInfo.split("\n")[1]
                #print(characterTags)
                characterName = entry[0:len(entry)-4:]
                completedCharacters.append(characterName)
                print(characterName)
                try:
                    franchisesFull[franchise].append(entry[0:len(entry)-4:])
                except:
                    franchisesFull[franchise] = []
                    franchisesFull[franchise].append(entry[0:len(entry)-4:])
            #print(entry[0:len(entry)-4:])
            try:
                franchise = characterInfo.split("\n")[1]
            except:
                print(characterInfo.split("\n")[0])
            #print(characterTags)
            try:
                franchisesAllNoFill[franchise].append(entry[0:len(entry)-4:])
            except:
                franchisesAllNoFill[franchise] = []
                franchisesAllNoFill[franchise].append(entry[0:len(entry)-4:])


for franchise in franchisesAllNoFill:
    filledOut = 0
    try:
        bob = str(len(franchisesFull[franchise]))
    except: 
        franchisesFull[franchise] = []
    franchiseInfo = franchise + " (" + str(len(franchisesFull[franchise])) + "/" + str(len(franchisesAllNoFill[franchise])) + ")"
    print(franchiseInfo)
writeFile1 = open("Characters\\franchises.txt", "w", encoding="utf8")
writeFile2 = open("Characters\\franchisesAll.txt", "w", encoding="utf8")

allFranchises = {}
for franchise in franchisesAllNoFill.keys():
    allFranchises[franchise] = franchisesAllNoFill[franchise]

franchiseAllCollections = []

for franchise in franchisesFull:
    franchiseInfo = franchise + " (" + str(len(franchisesFull[franchise])) + ")"
    writeFile1.write(franchiseInfo + "\n")
for franchise in franchisesAllNoFill:
    franchiseInfo = franchise + " (" + str(len(franchisesFull[franchise])) + "/" + str(len(franchisesAllNoFill[franchise])) + ")"
    writeFile2.write(franchiseInfo + "\n")

writeFile1.close()
writeFile2.close()

print("\n\n\n\n")
exitTest = ""

while exitTest != "End":
    exitTest = input("Enter a franchise: ")
    people = ""
    if exitTest != "End" and not(exitTest in allFranchises.keys()):
            print("Invalid franchise.")
    else:
        if exitTest != "End":
            people = str(exitTest) + ": "
            for person in allFranchises[exitTest]:
                if person in completedCharacters:
                    people = people + person + ", "
                else:
                    people = people + person + "(!), "
            print(people[0:len(people)-2:])