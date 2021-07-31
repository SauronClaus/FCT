import discord
from discord.utils import get

import random
import time
import os

from infoCard import infoPerson
from infoCard import infoArtifact

intents = discord.Intents.all()
client = discord.Client(intents=intents)

tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])

trueToken = testToken

switch = False
if switch == True:
    trueToken = botToken

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    #await client.get_user(self.user.id).edit(nick="FCT Test Bot")

    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "*testall" in message.content:
        name = message.content.split("-")[1]
        print(name)
        foundName = False

        alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # List all files in a directory using os.listdir
        for letter in alphabet:
            basepath = 'Characters/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    characterInfo = characterFile.read().split("\n")
                    if len(characterInfo) == 24:
                        if foundName == True:
                            embed = infoPerson(entry[0:len(entry)-4:])
                            await message.channel.send(embed=embed)
                            if characterInfo[22] != "":
                                for artifact in characterInfo[22].split("|"):
                                    embed = infoArtifact(artifact)
                                    await message.channel.send(embed=embed)
                        if entry[0:len(entry)-4:] == name:
                            foundName = True
                            
                        
        print("Completed!")
    if message.content == "*test artifacts":
        basepath = 'Artifacts/'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                if entry != "readMe.txt":
                    embed = infoArtifact(entry[0:len(entry)-4:])
                    await message.channel.send(embed=embed)
    if "*info" in message.content:
        messageParam = message.content[6::].split("-")
        if messageParam[0] == "artifact" or messageParam[0] == "Artifact":
            embed = infoArtifact(messageParam[1])
            await message.channel.send(embed=embed)
        if messageParam[0] == "person" or messageParam[0] == "Person":
            embed = infoPerson(messageParam[1])
            await message.channel.send(embed=embed)

client.run(trueToken)