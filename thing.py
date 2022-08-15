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

switch = False
if switch == True:
    trueToken = botToken

@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    #await client.get_user(self.user.).edit(nick="FCT Test Bot")

    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.id == userID:
        if "~testall" in message.content:
            print("Begin test all")
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
            print("Let's go")
            alphabet = ['#', "A", "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

            # List all files in a directory using os.listdir
            for letter in alphabet:
                basepath = 'Characters/' + letter
                for entry in os.listdir(basepath):
                    if os.path.isfile(os.path.join(basepath, entry)):
                        characterFile = open(basepath + "/" + entry, "r", encoding='utf8')
                        characterInfo = characterFile.read().split("\n")
                        if len(characterInfo) == 30:
                            if entry[0:len(entry)-4:] == name:
                                foundName = True
                            if foundName == True:
                                embed = infoPerson(entry[0:len(entry)-4:], "")
                                await message.channel.send(embed=embed)
                                if characterInfo[22] != "":
                                    for artifact in characterInfo[22].split("|"):
                                        embed = infoArtifact(artifact, "")
                                        await message.channel.send(embed=embed)
                            
                                
                            
            print("Completed!\n")
        if message.content == "~test artifacts":
            basepath = 'Artifacts/'
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    if entry != "readMe.txt":
                        embed = infoArtifact(entry[0:len(entry)-4:], message.channel)
                        await message.channel.send(embed=embed)
        if message.content == "~test franchises":

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
        if "~info" in message.content:
            print("Finding Info!")
            fctPolls = message.channel
            for channel in message.guild.text_channels:
                if channel.name == "fictional-competency-test-polls":
                    print("found #" + channel.name)
                    fctPolls = channel
            info = message.content[6::]
            if info[0:8:] == "artifact" or info[0:8:] == "Artifact":
                try:
                    artifactFile = open("Artifacts\\" + info[9:len(info):] + ".txt", "r", encoding='utf8')
                    embed = infoArtifact(info[9:len(info):], "")
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send("Couldn't find artifact " + info[9:len(info):] + ".")
            if info[0:6:] == "person" or info[0:6:] == "Person" or info[0:6:] == "People" or info[0:6:] == "people":
                try:
                    firstChar = info[7:8:]
                    if firstChar in numbers:
                        firstChar = "#"
                    personFile = open("Characters\\" + firstChar + "\\" + info[7:len(info)] + ".txt", "r", encoding='utf8')
                    embed = infoPerson(info[7:len(info):], "")
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send("Couldn't find person " + info[7:len(info):] + ".")
            if info[0:9:] == "franchise" or info[0:9:] == "Franchise":
                try:
                    firstChar = info[10:11:]
                    if firstChar in numbers:
                        firstChar = "#"
                    personFile = open("Franchises\\" + firstChar + "\\" + info[10:len(info):] + ".txt", "r", encoding='utf8')
                    embed = infoFranchise(info[10:len(info):], "")
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send("Couldn't find franchise " + info[10:len(info):] + ".")
            if info[0:9:] == "adjective" or info[0:9:] == "Adjective":
                try:
                    adjective = info[10:len(info):]
                    if adjective[len(adjective)-1::] != "-" and adjective[len(adjective)-1::] != " ":
                        adjective = adjective + " "
                    if adjective[len(adjective)-1::] != "-":
                        contentFile = open("Adjectives\\Descriptions\\" + adjective[:len(adjective)-1:] + ".txt", "r")
                    else:
                        contentFile = open("Adjectives\\Descriptions\\" + adjective + ".txt", "r")
                    embed = infoAdjective(info[10:len(info):], "")
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send("Couldn't find adjective " + info[10:len(info):] + ".")
            if info[0:7:] == "minions" or info[0:7:] == "Minions" or info[0:7:] == "minion" or info[0:7:] == "Minion":
                try:
                    artifactFile = open("Minions\\" + info[8:len(info):] + ".txt", "r", encoding='utf8')
                    embed = infoMinions(info[8:len(info):], "")
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send("Couldn't find minion " + info[8:len(info):] + ".")
            print("Completed!\n")
        if "~match" in message.content:
            matchSplit = message.content.split("match ")
            numberOfMatches = 1
            if len(matchSplit) > 1:
                numberOfMatches = int(matchSplit[1])
            for matchNum in range(1,numberOfMatches+1):
                print("Generating match!")
                replacement = generate(message.guild.id, matchNum-1)
                additives = replacement[4]

                people = allPeople()
                franchises = allFranchises()
                minions = allMinions()

                antagonistsReplacement = {}
                antagonistsReasonSubbing = {}
                antagonistsExist = False

                franchiseName = replacement[2][0]
                franchiseInfo = replacement[2][1]
                
                minionReplacements = {}
                minionReplaceReasons = {}
                minionAdjectives = {}
                
                minionsExist = False
                if replacement[3] != []:
                    print("Minions are true!")
                    minionsExist = True
                    minionReplacements = replacement[3][0]
                    minionReplaceReasons = replacement[3][1]
                    minionAdjectives = replacement[3][2]

                print("\n")
                if len(replacement[1]) == 5:
                    print("A " + str(len(replacement[1])) + " proves antagonists exist (out of 4)")
                    antagonistsReplacement = replacement[1][0]
                    antagonistsReasonSubbing = replacement[1][1]
                    antagonistsExist = True
                    antagonistAdjectives = replacement[1][3]
                    antagonistVersions = replacement[1][4]
                else:
                    print("A " + str(len(replacement[1])) + " proves antagonists don't exist")
                charactersReplacement = replacement[0][0]
                charactersReasonSubbing = replacement[0][1]
                protagonistAdjectives = replacement[0][3]
                protagonistVersions = replacement[0][4]

                embed = discord.Embed(title="Test", description="Test :)")

                origCharacters = {}
                subCharacters = {}

                origAntags = {}
                subAntags = {}
                adjectives = {}

                origMinions = {}
                subMinions = {}


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

                messageAdjectivesChannel = message.channel
                for channel in message.guild.text_channels:
                    if channel.name == "fictional-adjectives-info":
                        print("found #" + channel.name)
                        messageAdjectivesChannel = channel
                
                messageMinionsChannel = message.channel
                for channel in message.guild.text_channels:
                    if channel.name == "fictional-minions-info":
                        print("found #" + channel.name)
                        messageMinionsChannel = channel
                print("\n")

                for character in charactersReplacement.keys():
                    embed = infoPerson(character, fctPolls)
                    embedID = await(messagePeopleChannel.send(embed=embed))
                    origCharacters[character] = embedID
                    #print("Orig Protags: " + character + " = " + str(embedID.id))
                for character in charactersReplacement.values():
                    embed = infoPerson(character, fctPolls)
                    embedID = await(messagePeopleChannel.send(embed=embed))
                    subCharacters[character] = embedID
                    #print("Sub Protags: " + character + " = " + str(embedID.id))
                for adjective in protagonistAdjectives.values():
                    embed = infoAdjective(adjective, fctPolls)
                    embedID = await(messageAdjectivesChannel.send(embed=embed))
                    adjectives[adjective] = embedID
                
                if antagonistsExist == True:
                    for character in antagonistsReplacement.keys():
                        embed = infoPerson(character, fctPolls)
                        embedID = await(messagePeopleChannel.send(embed=embed))
                        origAntags[character] = embedID
                        #print("Orig Antags: " + character + " = " + str(embedID.id))
                    for character in antagonistsReplacement.values():
                        embed = infoPerson(character, fctPolls)
                        embedID = await(messagePeopleChannel.send(embed=embed))
                        subAntags[character] = embedID
                        #print("Sub Antags: " + character + " = " + str(embedID.id))
                    for adjective in antagonistAdjectives.values():
                        embed = infoAdjective(adjective, fctPolls)
                        embedID = await(messageAdjectivesChannel.send(embed=embed))
                        adjectives[adjective] = embedID

                if minionsExist == True:
                    for minion in minionReplacements.keys():
                        embed = infoMinions(minion, fctPolls)
                        embedID = await(messageMinionsChannel.send(embed=embed))
                        origMinions[minion] = embedID
                        if minion in minionReplacements.values():
                            subMinions[minion] = embedID
                    for minion in minionReplacements.values():
                        if not(minion in minionReplacements.keys()):
                            embed = infoMinions(minion, fctPolls)
                            embedID = await(messageMinionsChannel.send(embed=embed))
                            subMinions[minion] = embedID
                    for adjective in minionAdjectives.values():
                        embed = infoAdjective(adjective, fctPolls)
                        embedID = await(messageAdjectivesChannel.send(embed=embed))
                        adjectives[adjective] = embedID

                embed = discord.Embed(title="Test", description="Test :)")
                print("\n")
                embed = infoFranchise(franchiseName, fctPolls)
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
                    subVersion = ""
                    try:
                        subVersion = " (" + protagonistVersions[subCharacter] + ") "
                    except:
                        print(subCharacter + " has no versions!")
                        print(str(protagonistVersions))
                    try:
                        additive = ""
                        try:
                            additive = "(" + additives[protagonist] + ") "
                        except:
                            zeff = 0
                        adjective = protagonistAdjectives[subCharacter]
                        if charactersReasonSubbing[protagonist][0] == "Full Random":
                            replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0]
                        else:
                            if charactersReasonSubbing[protagonist][0] == "No Change":
                                replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") " + subVersion + " doesn't change."
                            else:
                                if charactersReasonSubbing[protagonist][0] == "Ages":
                                    if charactersReasonSubbing[protagonist][1].split("|")[1] == "1":
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0][0:len(charactersReasonSubbing[protagonist][1].split("|")[0])-1:] + ")"
                                    else:
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0] + ")"
                                else:
                                    replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
                        
                        if len(replacementLines) + len(replacementText) >= 1024:
                            replacementList.append(replacementLines)
                            replacementLines = ""
                        replacementLines = replacementLines + "-" + replacementText + "\n"
                    except:
                        if charactersReasonSubbing[protagonist][0] == "Full Random":
                            replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0]
                        else:
                            if charactersReasonSubbing[protagonist][0] == "No Change":
                                replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ")" + subVersion + " doesn't change."
                            else:
                                if charactersReasonSubbing[protagonist][0] == "Ages":
                                    if charactersReasonSubbing[protagonist][1].split("|")[1] == "1":
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0][0:len(charactersReasonSubbing[protagonist][1].split("|")[0])-1:] + ")"
                                    else:
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0] + ")"
                                else:
                                    replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
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
                        additive = ""
                        try:
                            additive = "(" + additives[antagonist] + ") "
                        except:
                            zef = 0
                        subCharacter = antagonistsReplacement[antagonist]
                        subVersion = ""
                        try:
                            subVersion = " (" + antagonistVersions[subCharacter] + ") "
                        except:
                            print(subCharacter + " has no versions!")
                        try:
                            adjective = antagonistAdjectives[subCharacter]
                            if antagonistsReasonSubbing[antagonist][0] == "Full Random":
                                replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0]
                            else:
                                if antagonistsReasonSubbing[antagonist][0] == "No Change":
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") " + subVersion + " doesn't change."
                                else:
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1] + ")"
                        except:
                            if antagonistsReasonSubbing[antagonist][0] == "Full Random":
                                replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0]
                            else:
                                if antagonistsReasonSubbing[antagonist][0] == "No Change":
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") " + subVersion + " doesn't change."
                                else:
                                    if antagonistsReasonSubbing[antagonist][0] == "Ages":
                                        if antagonistsReasonSubbing[antagonist][1].split("|")[1] == "1":
                                            replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1].split("|")[1] + " " + antagonistsReasonSubbing[antagonist][1].split("|")[0][0:len(antagonistsReasonSubbing[antagonist][1].split("|")[0])-1:] + ")"
                                        else:
                                            replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1].split("|")[1] + " " + antagonistsReasonSubbing[antagonist][1].split("|")[0] + ")"
                                    else:
                                        replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1] + ")"
                        
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
                            print("Added antagonists to embed")
                        i+=1
                
                if minionsExist == True:
                    replacementLines = ""
                    replacementList = []
                    #minionReplacements = {}
                    #minionReplaceReasons = {}
                    #minionAdjectives = {}
                    for minion in minionReplacements.keys():
                        try:
                            adjective = minionAdjectives[minion]
                            if minionReplaceReasons[minion][0] == "Full Random":
                                replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0]
                            else:
                                if minionReplaceReasons[minion][0] == "No Change":
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") didn't change."
                                else:
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")"
                        except:
                            if minionReplaceReasons[minion][0] == "Full Random":
                                print("[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ")")
                                print(minions[minionReplacements[minion]][0])
                                print(minion + ": ")
                                print(str(minionReplacements))
                                print(str(subMinions))
                                print(str(minionReplacements[minion]))
                                print("is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ")")
                                print("via " + minionReplaceReasons[minion][0])
                                replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0]
                            else:
                                if minionReplaceReasons[minion][0] == "No Change":
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") didn't change."
                                else:
                                    print("[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ")")
                                    print(minions[minionReplacements[minion]][0])
                                    print(minion + ": ")
                                    print(str(minionReplacements))
                                    print(str(subMinions))
                                    print(str(minionReplacements[minion]))
                                    print(str(subMinions[minionReplacements[minion]].id))
                                    print("is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ")")
                                    print("via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")")

                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(message.channel.guild.id) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")"
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
                            embed.add_field(name="Minions #" + str(i), value=embedFieldProtag, inline=False)
                        else:
                            embed.add_field(name="Minions", value=embedFieldProtag, inline=False)

                        i+=1
                    
                
                
                if franchiseInfo[2] != "":
                    embed.set_thumbnail(url=franchiseInfo[2])
                embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
                embed.color = colors[franchiseInfo[15]]

                finalMessage = await fctPolls.send(embed=embed)
                await finalMessage.add_reaction(emoji="✅")
                await finalMessage.add_reaction(emoji="🌐")
                await finalMessage.add_reaction(emoji="❎")

                print("\nCompleted Match #" + str(matchNum) + "!\n")
                print("Had " + str(len(protagonistAdjectives)) + " adjectives.")
            if fctPolls.id == 523962430179770369 and fctPolls.id == 876602515372781679 and matchNum == 5:
                await fctPolls.send("<@&613144506757283974>")
            print("\nCompleted all!")
        if message.content == "~test minions":
            # List all files in a directory using os.listdir
            basepath = 'Minions/'
            for entry in os.listdir(basepath):
                if os.path.isfile(os.path.join(basepath, entry)):
                    print(entry)
                    franchiseFile = open(basepath + "/" + entry, "r", encoding='utf8')
                    franchiseInfo = franchiseFile.read().split("\n")
                    if len(franchiseInfo) == 24:
                        embed = infoMinions(entry[0:len(entry)-4:], message.channel)
                        await message.channel.send(embed=embed)
        if "~group" in message.content:
            groupName = message.content[7:len(message.content):]
            groups = allGroups()
            for person in groups[groupName]:
                print("Found " + person + "!")
                embed = infoPerson(person, "")
                await message.channel.send(embed=embed)
            print("Completed!\n")

client.run(trueToken)