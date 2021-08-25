# Prints every character out into charactersList.txt with their name (as in line 1 of their file) followed by their file's name.
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
import os

charactersCompleted = []

# List all files in a directory using os.listdir
for letter in alphabet:
    basepath = 'Characters/' + letter
    for entry in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, entry)):
            characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
            characterInfo = characterFile.read().split("\n")
            if len(characterInfo) == 29:
                charactersCompleted.append(characterInfo[0] + " (" + entry[0:len(entry)-4:] + ")")

charactersWriteFile = open("charactersList.txt", "w", encoding='utf8')
for character in charactersCompleted:
    charactersWriteFile.write(character + "\n")