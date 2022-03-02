#Locates all the characters of a particular franchise, and performs the notepad thing on them for ease of editing.
import os
import psutil
import time
import discord

print("Begin test all")


intents = discord.Intents.all()
client = discord.Client(intents=intents)

tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])

trueToken = testToken

switch = True
if switch == True:
    trueToken = botToken

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    #await client.get_user(self.user.).edit(nick="FCT Test Bot")
    foundName = True
    print("Let's go")
    alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    raritiesToNumbers = {
        "High": 3,
        "Medium": 2,
        "Low": 1,
        "Very Low": 0.5, 
        "Very Low*": 0.1,
        "High": 3.0,
        "Medium": 2.0,
        "Low": 1.0,
        "Very Low": 0.5, 
        "Very Low*": 0.1
    }
    franchisesCharacters = {}
    franchises = []
    franchiseRarities = {}
    x = 0
    for letter in alphabet:
        basepath = 'Characters/' + letter
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                characterInfo = characterFile.read().split("\n")
                if len(characterInfo) == 30:
                    #print(characterInfo[0])
                    if characterInfo[1] in franchises:
                        franchisesCharacters[characterInfo[1]].append(characterInfo[0])
                        franchiseRarities[characterInfo[1]][0]+=raritiesToNumbers[characterInfo[17]]
                        franchiseRarities[characterInfo[1]][1]+=1
                        #print(characterInfo[1])
                    if not characterInfo[1] in franchises:
                        franchises.append(characterInfo[1])
                        franchisesCharacters[characterInfo[1]] = [characterInfo[0]]
                        franchiseRarities[characterInfo[1]] = [raritiesToNumbers[characterInfo[17]], 1]
                    
            x+=1
            if x%300 == 0:
                print(str(x) + " people found!")

    franchises.sort()
    print("Found " + str(len(franchises)) + " franchises!")
    channel = client.get_channel(948259558592229436)
    for franchiseNum in range(len(franchises)):
        string = " ("
        for character in franchisesCharacters[franchises[franchiseNum]]:
            string = string + character + ", "
        string = string[0:len(string)-2:] + ")"
        averageRarity = franchiseRarities[franchises[franchiseNum]][0]/franchiseRarities[franchises[franchiseNum]][1]
        
        print("Franchise #" + str(franchiseNum) + ": " + franchises[franchiseNum] + string + " [Average Rarity: " + str(round(averageRarity,2)) + "]")
        message = await channel.send("Franchise #" + str(franchiseNum) + ": " + franchises[franchiseNum] + string + " [Average Rarity: " + str(round(averageRarity,2)) + "]")
        await message.add_reaction("⬆")
        await message.add_reaction("🆗")
        await message.add_reaction("⬇")


    print("Completed!")

client.run(trueToken)