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
    file = open("Franchises to Change.txt", "w", encoding='utf8')
    x = 0
    pollChannel = client.get_channel(948259558592229436)
    async for message in pollChannel.history(limit=None):
        if message.reactions != []:
            print(str(message.reactions))
            reactions = {
                "⬆": [],
                "🆗": [],
                "⬇": []
            }
            upQuant = 0
            okQuant = 0
            downQuant = 0
            
            for reaction in message.reactions:
                if reaction.emoji == "⬆":
                    upQuant+=reaction.count
                if reaction.emoji == "🆗":
                    okQuant+=reaction.count
                if reaction.emoji == "⬇":
                    downQuant+=reaction.count
            async for reaction in message.users():
                
            file.write("[" + str(upQuant-1) + "-" + str(okQuant-1) + "-" + str(downQuant-1) + "] " + message.content + "\n" + "\t[" + str(upQuant-1) +  + "-" + str(okQuant-1) + "-" + str(downQuant-1) + "] ")

    file.close()

    print("Completed!")

client.run(trueToken)