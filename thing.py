import discord
from discord.utils import get

import random
import time

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
    if message.content == "*test":
        embed = infoPerson("Captain Nemo")
        await message.channel.send(embed=embed)

        embed = infoArtifact("The Nautilus")
        await message.channel.send(embed=embed)
        

client.run(trueToken)