import os
artifactNum = 0
basepath = "Artifacts\\"
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        artifactFile = open(basepath + "/" + entry, "r", encoding='utf8')
        artifactInfo = artifactFile.read().split("\n")
        if len(artifactInfo) == 14:
            artifactNum+=1
print(artifactNum)