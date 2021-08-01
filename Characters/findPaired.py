alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


import os

groupsLarge = {}

writeFile = open("Characters\\duos.txt","w",encoding='utf8')
write2File = open("Characters\\duosAll.txt","w",encoding='utf8')

duoSeconds = []
print("Start!")

duos = {}
# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                tags = characterInfo[15].split(",")
                for tag in tags:
                    tagWithDuo = tag.split("|")
                    if len(tagWithDuo) == 2:
                        #print(tag)
                        write2File.write(characterInfo[0] + ": " + tagWithDuo[1] + " (" + tagWithDuo[0] + ")\n")
                        duos[tagWithDuo[1]] = characterInfo[0]
                        duoSeconds.append(tagWithDuo[1])
            if len(characterInfo) == 17 or len(characterInfo) == 17:
                print("(*) " + entry[0:len(entry)-4:])

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 24:
                if entry[0:len(entry)-4:] in duoSeconds:
                    print(entry[0:len(entry)-4:])
                    print(duos[entry[0:len(entry)-4:]] + " found!")
                    del duos[entry[0:len(entry)-4:]]
                    duoSeconds.remove(entry[0:len(entry)-4:])   

duosFirsts = []

for d in duos.keys():
    duosFirsts.append(str(d))

duosFirsts.sort()
for duo in duosFirsts:
    writeFile.write(duo + "\n")

print("Completed!")