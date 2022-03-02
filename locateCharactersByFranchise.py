#Locates all the characters of a particular franchise, and performs the notepad thing on them for ease of editing.
import os
import psutil
import time

print("Begin test all")


foundName = True
print("Let's go")
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
franchiseToFind = "RWBY"
x = 0
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 30 and characterInfo[1] == franchiseToFind:
                os.startfile(basepath + "\\" + entry)
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
        x+=1
        if x%100 == 0:
            print(str(x) + " people found!")
print("Completed!")