numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

import os

while True == True:
    fileName = input("Enter file name: ")
    firstLetter = fileName[0:1:]
    if firstLetter in numbers:
        firstLetter = "#"
    try:
        os.startfile("Characters\\" + firstLetter + "\\" + fileName + ".txt")
    except:
        print("Couldn't find file")