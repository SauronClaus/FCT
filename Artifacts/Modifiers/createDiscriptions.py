import os

basepath = 'Artifacts\\Modifiers\\Additions\\'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        tierFile = open(os.path.join(basepath, entry), "r")
        objects = tierFile.read().split("\n")
        for object in objects:
            print("<" + object[:len(object)-1] + ">")
            if not(os.path.isfile(os.path.join("Artifacts\\Modifiers\\Descriptions\\", object[:len(object)-1] + ".txt"))) and object[:len(object)-2:] != "":
                newFile = open("Artifacts\\Modifiers\\Descriptions\\" + object[:len(object)-2:] + ".txt", "w")
                newFile.write(object[:len(object)-2:])
                newFile.close()
        tierFile.close()

basepath = 'Artifacts\\Modifiers\\Adjectives\\'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        tierFile = open(os.path.join(basepath, entry), "r")
        objects = tierFile.read().split("\n")
        for object in objects:
            print("<" + object[:len(object)-1] + ">")
            artifactName = object[:len(object)-1]
            if "|" in artifactName:
                artifactName = artifactName.split("|")[0]
                artifactName = artifactName[:len(artifactName)-1:]
            if not(os.path.isfile(os.path.join("Artifacts\\Modifiers\\Descriptions\\", artifactName))) and artifactName != "":
                newFile = open("Artifacts\\Modifiers\\Descriptions\\" + artifactName + ".txt", "w")
                newFile.write(artifactName)
                newFile.close()
        tierFile.close()