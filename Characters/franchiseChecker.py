# Alright, so basically this file allows you to check the franchises associated with a person.
# So it prints out, and prints into franchisesAll.txt, a list of every franchise with the associated 
# number of people under the number of valid people. 

alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
oldCompletedCharacters = {}
newCompletedCharacters = {}
allCharacters = {}
completedCharactersOld = []
completedCharactersNew = []
import os

print("Start!")
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read()
            #print(characterInfo.split("\n")[0])
            if len(characterInfo.split("\n")) == 17:
                #print(entry[0:len(entry)-4:])
                franchise = characterInfo.split("\n")[1]
                #print(franchise)
                characterName = entry[0:len(entry)-4:]
                completedCharactersOld.append(characterName)
                print(characterName)
                try:
                    oldCompletedCharacters[franchise].append(entry[0:len(entry)-4:])
                except:
                    oldCompletedCharacters[franchise] = []
                    oldCompletedCharacters[franchise].append(entry[0:len(entry)-4:])
            #print(entry[0:len(entry)-4:])
            if len(characterInfo.split("\n")) == 22:
                #print(entry[0:len(entry)-4:])
                franchise = characterInfo.split("\n")[1]
                #print(franchise)
                characterName = entry[0:len(entry)-4:]
                completedCharactersNew.append(characterName)
                print(characterName)
                try:
                    newCompletedCharacters[franchise].append(entry[0:len(entry)-4:])
                except:
                    newCompletedCharacters[franchise] = []
                    newCompletedCharacters[franchise].append(entry[0:len(entry)-4:])
            try:
                franchise = characterInfo.split("\n")[1]
            except:
                print(characterInfo.split("\n")[0])
                #print(franchise)
            try:
                allCharacters[franchise].append(entry[0:len(entry)-4:])
            except:
                allCharacters[franchise] = []
                allCharacters[franchise].append(entry[0:len(entry)-4:])


for franchise in allCharacters:
    filledOut = 0
    try:
        bob = str(len(oldCompletedCharacters[franchise]))
    except: 
        oldCompletedCharacters[franchise] = []
    try:
        joe = str(len(newCompletedCharacters[franchise]))
    except: 
        newCompletedCharacters[franchise] = []
    franchiseInfo = franchise + " (" + str(len(newCompletedCharacters[franchise])) + "/" + str(len(oldCompletedCharacters[franchise])) + "/" + str(len(allCharacters[franchise])) + ")"
    print(franchiseInfo)
writeFile1 = open("Characters\\franchises.txt", "w", encoding="utf8")
writeFile2 = open("Characters\\franchisesAll.txt", "w", encoding="utf8")

allFranchises = {}
for franchise in allCharacters.keys():
    allFranchises[franchise] = allCharacters[franchise]

franchiseAllCollections = []

for franchise in oldCompletedCharacters:
    franchiseInfo = franchise + " (" + str(len(oldCompletedCharacters[franchise])) + ")"
    writeFile1.write(franchiseInfo + "\n")
for franchise in allCharacters:
    franchiseInfo = franchise + " (" + str(len(newCompletedCharacters[franchise])) + "/" + str(len(oldCompletedCharacters[franchise])) + "/" + str(len(allCharacters[franchise])) + ")"
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
                if person in completedCharactersNew:
                    people = people + person + ", "
                else:
                    if person in completedCharactersOld:
                        people = people + person + "(*), "
                    else:
                        people = people + person + "(!), "
            print(people[0:len(people)-2:])