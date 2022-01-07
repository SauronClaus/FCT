import os
import psutil
import time

print("Begin test all")


foundName = True
print("Let's go")
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 29:
                os.startfile(basepath + "\\" + entry)
                if characterInfo[27] != "":
                    print(entry + ": " + characterInfo[27])
                else:
                    print(entry)
                #print("Next step")
                loopquant = 0
                notepad = True
                while notepad == True:
                    if loopquant > 3:
                        time.sleep(1)
                    else:
                        time.sleep(0.1)
                    notepad = False
                    for i in psutil.process_iter():
                        if i.name() == "notepad.exe":
                            notepad = True
                    loopquant +=1

                