# The main file for the bot. 
import discord
from discord.utils import get

import random
import time
import os

from infoCard import infoPerson
from infoCard import infoFranchise
from infoCard import infoArtifact
from infoCard import infoAdjective
from infoCard import infoMinions

from generation import generate
from colors import colors

from all import allMinions
from all import allPeople
from all import allFranchises
from all import allGroups

from generateAllPeople import genMinions
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


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
if switch == False:
    trueToken = botToken

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    #await client.get_user(self.user.id).edit(nick="FCT Test Bot")

    

@client.event
async def on_typing(channel, user, when):
    await channel.send(user.name + " is typing!")
client.run(trueToken)