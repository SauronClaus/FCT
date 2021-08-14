import discord
from discord.utils import get

import random
import time
import os

from infoCard import infoPerson
from infoCard import infoFranchise
from infoCard import infoArtifact

from generation import generate
from colors import colors


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
        foundName = False
        name = ""
        messageList = message.content.split("-")
        if len(messageList) > 1:
            name = messageList[1]
            print(name)
            foundName = False
        else:
            print("No name detected; starting from beginning")
            foundName = True

        alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # List all files in a directory using os.listdir
        for letter in alphabet:
            basepath = 'Characters/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    characterInfo = characterFile.read().split("\n")
                    if len(characterInfo) == 24:
                        if entry[0:len(entry)-4:] == name:
                            foundName = True
                        if foundName == True:
                            embed = infoPerson(entry[0:len(entry)-4:])
                            await message.channel.send(embed=embed)
                            if characterInfo[22] != "":
                                for artifact in characterInfo[22].split("|"):
                                    embed = infoArtifact(artifact)
                                    await message.channel.send(embed=embed)
                        
                            
                        
        print("Completed!")
    if message.content == "*test artifacts":
        basepath = 'Artifacts/'
        for entry in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, entry)):
                if entry != "readMe.txt":
                    embed = infoArtifact(entry[0:len(entry)-4:])
                    await message.channel.send(embed=embed)
    if message.content == "*test franchises":

        alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

        # List all files in a directory using os.listdir
        for letter in alphabet:
            basepath = 'Franchises/' + letter
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    print(entry)
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read().split("\n")
                    if len(franchiseInfo) == 16:
                        embed = infoFranchise(entry[0:len(entry)-4:])
                        await message.channel.send(embed=embed)
    if "*info" in message.content:
        messageParam = message.content[6::].split("-")
        if messageParam[0] == "artifact" or messageParam[0] == "Artifact":
            embed = infoArtifact(messageParam[1])
            await message.channel.send(embed=embed)
        if messageParam[0] == "person" or messageParam[0] == "Person":
            embed = infoPerson(messageParam[1])
            await message.channel.send(embed=embed)
    if "*match" in message.content:
        matchSplit = message.content.split("match ")
        numberOfMatches = 1
        if len(matchSplit) > 1:
            numberOfMatches = int(matchSplit[1])
        for matchNum in range(1,numberOfMatches+1):
            print("Generating match!")
            replacement = generate()

            antagonistsReplacement = {}
            antagonistsReasonSubbing = {}
            antagonistsExist = False

            franchiseName = replacement[2][0]
            franchiseInfo = replacement[2][1]
            print("\n")
            if len(replacement[1]) == 3:
                print(str(len(replacement[1])) + " proves antags exist")
                antagonistsReplacement = replacement[1][0]
                antagonistsReasonSubbing = replacement[1][1]
                antagonistsExist = True
            else:
                print(str(len(replacement[1])) + " proves antags don't exist")
            charactersReplacement = replacement[0][0]
            charactersReasonSubbing = replacement[0][1]

            embed = discord.Embed(title="Test", description="Test :)")

            origCharacters = {}
            subCharacters = {}

            origAntags = {}
            subAntags = {}
            messagePeopleChannel = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "fictional-people-info":
                    print("found #" + channel.name)
                    messagePeopleChannel = channel

            messageFranchiseChannel = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "franchises-info":
                    print("found #" + channel.name)
                    messageFranchiseChannel = channel

            fctPolls = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "fictional-competency-test-polls":
                    print("found #" + channel.name)
                    fctPolls = channel

            for character in charactersReplacement.keys():
                embed = infoPerson(character)
                embedID = await(messagePeopleChannel.send(embed=embed))
                origCharacters[character] = embedID
                print("Orig Protags: " + character + " = " + str(embedID.id))
            for character in charactersReplacement.values():
                embed = infoPerson(character)
                embedID = await(messagePeopleChannel.send(embed=embed))
                subCharacters[character] = embedID
                print("Sub Protags: " + character + " = " + str(embedID.id))

            
            if antagonistsExist == True:
                for character in antagonistsReplacement.keys():
                    embed = infoPerson(character)
                    embedID = await(messagePeopleChannel.send(embed=embed))
                    origAntags[character] = embedID
                    print("Orig Antags: " + character + " = " + str(embedID.id))
                for character in antagonistsReplacement.values():
                    embed = infoPerson(character)
                    embedID = await(messagePeopleChannel.send(embed=embed))
                    subAntags[character] = embedID
                    print("Sub Antags: " + character + " = " + str(embedID.id))


            embed = discord.Embed(title="Test", description="Test :)")
            embed = infoFranchise(franchiseName)
            franchiseID = await(messageFranchiseChannel.send(embed=embed))

            testString = "[" + franchiseInfo[0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageFranchiseChannel.id) + "/" + str(franchiseID.id) + ")"
            #print("Test String: " + testString + " (" + str(len(testString)) + ")")
            if numberOfMatches == 1:
                embed = discord.Embed(title=franchiseInfo[0],description=testString)
            else:
                embed = discord.Embed(title="Match #" + str(matchNum) + ": " + franchiseInfo[0],description=testString)

            
            replacementLines = ""
            replacementList = []
            for protagonist in charactersReplacement.keys():
                subCharacter = charactersReplacement[protagonist]
                #print(protagonist + ": " + "(https://discord.com/channels/" + str(message.channel.id) + "/" + str(origCharacters[protagonist].id) + ")")
                #print(subCharacter + ": " + "(https://discord.com/channels/" + str(message.channel.id) + "/" + str(subCharacters[subCharacter].id) + ")")
                #print(str(charactersReasonSubbing))
                
                #print(charactersReasonSubbing[protagonist][0] + ": " + charactersReasonSubbing[protagonist][1] + "")
                if charactersReasonSubbing[protagonist][0] == "Full Random":
                    replacementText = "[" + protagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") via " + charactersReasonSubbing[protagonist][0]
                    print(subCharacter + "[" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ")")
                else:
                    if charactersReasonSubbing[protagonist][0] == "No Change":
                        replacementText = "[" + protagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") doesn't change."
                        print(subCharacter + "[" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ")")
                    else:
                        replacementText = "[" + protagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
                        print(subCharacter + "[" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ")")
                #replacementText = protagonist + " is replaced by " + subCharacter + " via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
                #print(replacementText + " (" + str(len(replacementText)) + ")")
                if len(replacementLines) + len(replacementText) >= 1024:
                    replacementList.append(replacementLines)
                    replacementLines = ""
                replacementLines = replacementLines + "-" + replacementText + "\n"
            replacementList.append(replacementLines)
            i = 1
            for embedFieldProtag in replacementList:
                embedFieldProtag = embedFieldProtag[0:len(embedFieldProtag)-1:]
                #print("Embed Field #" + str(i) + ": " + embedFieldProtag + " (" + str(len(embedFieldProtag)) + ")")
                if len(replacementList) > 1:
                    embed.add_field(name="Protagonists #" + str(i), value=embedFieldProtag, inline=False)
                else:
                    embed.add_field(name="Protagonists", value=embedFieldProtag, inline=False)

                i+=1
            
            if antagonistsExist == True:
                replacementLines = ""
                replacementList = []
                for antagonist in antagonistsReplacement.keys():
                    subCharacter = antagonistsReplacement[antagonist]
                    if antagonistsReasonSubbing[antagonist][0] == "Full Random":
                        replacementText = "[" + antagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") via " + antagonistsReasonSubbing[antagonist][0]
                    else:
                        if antagonistsReasonSubbing[antagonist][0] == "No Change":
                            replacementText = "[" + antagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") doesn't change."
                        else:
                            replacementText = "[" + antagonist + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + subCharacter + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1] + ")"
                    
                    #print(replacementText + " (" + str(len(replacementText)) + ")")
                    if len(replacementLines) + len(replacementText) >= 1024:
                        replacementList.append(replacementLines)
                        replacementLines = ""
                    replacementLines = replacementLines + "-" + replacementText + "\n"
                replacementList.append(replacementLines)
                i = 1
                for embedFieldAntag in replacementList:
                    embedFieldAntag = embedFieldAntag[0:len(embedFieldAntag)-1:]
                    if len(replacementList) > 1:
                        embed.add_field(name="Antagonists #" + str(i), value=embedFieldAntag, inline=False)
                    else:
                        embed.add_field(name="Antagonists", value=embedFieldAntag, inline=False)
                    i+=1
            
            
            if franchiseInfo[2] != "":
                embed.set_thumbnail(url=franchiseInfo[2])
            embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
            embed.color = colors[franchiseInfo[14]]

            finalMessage = await fctPolls.send(embed=embed)
            await finalMessage.add_reaction(emoji="✅")
            await finalMessage.add_reaction(emoji="🌐")
            await finalMessage.add_reaction(emoji="❎")

            print("\nCompleted Match #" + str(matchNum) + "!")
        print("\nCompleted all!")





client.run(trueToken)