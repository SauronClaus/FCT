alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
tagsFull = {}
import os

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read()
           
            if len(characterInfo.split("\n")) > 3:
                print(entry[0:len(entry)-4:])
                characterTags = characterInfo.split("\n")[13]
                #print(characterTags)
                tags = characterTags.split(",")
                for tagWithInfo in tags: 
                    tag = tagWithInfo.split("|")[0]
                    try:
                        tagsFull[tag].append(entry[0:len(entry)-4:])
                    except:
                        tagsFull[tag] = []
                        tagsFull[tag].append(entry[0:len(entry)-4:])

writeFile = open("Characters\\tags.txt", "w", encoding="utf8")
for tag in tagsFull:
    tagInfo = tag + " (" + str(len(tagsFull[tag])) + ")"
    writeFile.write(tagInfo + "\n")
writeFile.close()

print("\n\n\n\n")
exitTest = ""
while exitTest != "End":
    exitTest = input("Enter a tag: ")
    people = ""
    if exitTest != "End" and not(exitTest in tagsFull.keys()):
            print("Invalid tag.")
    else:
        if exitTest != "End":
            people = str(exitTest) + ": "
            for person in tagsFull[exitTest]:
                people = people + person + ", "
            print(people[0:len(people)-2:])
        
    
    
