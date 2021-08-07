alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

searchColor = "--"
colorList = {}

currentColorsFile = open("colors.txt", "r", encoding='utf8')
currentColors = currentColorsFile.read().split("\n")
currentColorList = []
for colors in currentColors:
    if colors != "":
        color = colors.split('"')[1]
        #print(color)
        currentColorList.append(color)

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
                    characterColor = characterInfo[23]
                    if not(characterColor in currentColorList):
                        print("New Color! " + characterColor)
                    if characterColor == searchColor:
                        print(entry)

                    try:
                        colorList[characterColor]+=1
                    except:
                        colorList[characterColor] = 1
                except:
                    print(entry + " is broken!")

basepath = "Artifacts\\"
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        artifactFile = open(basepath + "/" + entry, "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")
        if len(artifactInfo) == 14:
            #print(entry + ": " + str(len(characterInfo)))
            try:
                artifactColor = artifactInfo[13]
                if artifactColor == searchColor:
                        print(entry)
                try:
                    colorList[artifactColor]+=1
                except:
                    colorList[artifactColor] = 1
            except:
                print(entry + " is broken!")
                
colorFile = open("colors.txt","w")
for color in colorList.keys():
    colorFile.write('"' + color + '": "' + str(colorList[color]) + '",\n')
                
