alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


import os

groupsLarge = {}

writeFile = open("addBeforeItBreaks.txt","w",encoding='utf8')
write2File = open("franchiseCharacters.txt","w",encoding='utf8')
franchiseCharacterFile = open("neededCharacters.txt","w",encoding='utf8')

franchiseSearch = ["NieR:Automata", "Stormlight Archive", "Mistborn"]
franchiseAddCharacters = []

charactersToFind = []

artifactList = []
artifactsIncomplete = []

print("Start!")
numberFranchises = 0
numberOfFranchises = 0
listFranchises = ""
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Franchises/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
            franchiseInfo = franchiseFile.read().split("\n")
            if len(franchiseInfo) >= 8:
                numberOfFranchises +=1
                numberFranchises +=1
                listFranchises = listFranchises + franchiseInfo[0] + ", "
                characters = franchiseInfo[7].split("|")
                characterString = ""
                for character in characters:
                    charactersToFind.append(character)
                    characterString = characterString + character + ", "
                    if franchiseInfo[0] in franchiseSearch:
                        franchiseAddCharacters.append(character)
                if len(franchiseInfo) == 16:
                    if franchiseInfo[8] != "":
                        antagonists = franchiseInfo[8].split("|")
                        for antagonist in antagonists:
                            charactersToFind.append(character)
                            characterString = characterString + antagonist + ", "
                            if franchiseInfo[0] in franchiseSearch:
                                franchiseAddCharacters.append(antagonist)
                    if franchiseInfo[9] != "":
                        artifacts = franchiseInfo[9].split("|")
                        for artifact in artifacts:
                            artifactList.append(artifact)
                            artifactsIncomplete.append(artifact)
                            print("Artifact: " + artifact)
                write2File.write(franchiseInfo[0] + ": " + characterString[0:len(characterString)-2:] + "\n")

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                if entry[0:len(entry)-4:] in charactersToFind:
                    while entry[0:len(entry)-4:] in charactersToFind:
                        #print(entry[0:len(entry)-4:])
                        charactersToFind.remove(entry[0:len(entry)-4:])   
basepath = 'Artifacts'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        try:
            artifactFile = open(basepath + "/" + entry, "r", encoding='utf8')
            artifactInfo = artifactFile.read().split("\n")
            if len(artifactInfo) == 14:
                artifactsIncomplete.remove(entry[0:len(entry)-4:])
        except:
            print("Incomplete: " + entry[0:len(entry)-4:])

for artiafct in artifactsIncomplete:
    print("+" + artiafct)

singular = []
charactersToFind.sort()

for character in charactersToFind:
    if not(character in singular):
        singular.append(character)

for character in singular:
    if not(character in franchiseAddCharacters):
        writeFile.write("Character: " + character + "\n")

for character in franchiseAddCharacters:
    franchiseCharacterFile.write(character + "\n")
artifactsIncomplete.sort()
for artifact in artifactsIncomplete:
    writeFile.write("Artifact: " + artifact + "\n")

print("Franchises (" + str(numberFranchises) + "): " + listFranchises[0:len(listFranchises)-2:])
print("Completed!")
