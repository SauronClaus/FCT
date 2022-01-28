# The main file for the bot. 
import discord

from infoCard import infoPerson
from infoCard import infoFranchise
from infoCard import infoAdjective
from infoCard import infoMinions

from generation import generate
from colors import colors

from all import allMinions
from all import allPeople
from all import allFranchises

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


intents = discord.Intents.all()
client = discord.Client(intents=intents)

tokenFile = open("token.txt", "r")
tokenString = tokenFile.read()
tokens = tokenString.split('\n')
botToken = tokens[1]
testToken = tokens[0]
userID = int(tokens[2])

trueToken = botToken


guildID = 620964009247768586
defaultChannel = client.get_channel(620964009679650847)
#Test guild, currently


@client.event
async def on_ready(): 
    print('Logged in as {0.user}'.format(client))
    guild = client.get_guild(guildID)
    if True == True:
        if False == False:
            for matchNum in range(5):
                print("Generating match!")
                replacement = generate(guild.id)
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


                messagePeopleChannel = defaultChannel
                for channel in guild.text_channels:
                    if channel.name == "fictional-people-info":
                        print("found #" + channel.name)
                        messagePeopleChannel = channel

                messageFranchiseChannel = defaultChannel
                for channel in guild.text_channels:
                    if channel.name == "franchises-info":
                        print("found #" + channel.name)
                        messageFranchiseChannel = channel

                fctPolls = defaultChannel
                for channel in guild.text_channels:
                    if channel.name == "fictional-competency-test-polls":
                        print("found #" + channel.name)
                        fctPolls = channel

                messageAdjectivesChannel = defaultChannel
                for channel in guild.text_channels:
                    if channel.name == "fictional-adjectives-info":
                        print("found #" + channel.name)
                        messageAdjectivesChannel = channel
                
                messageMinionsChannel = defaultChannel
                for channel in guild.text_channels:
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

                testString = "[" + franchiseInfo[0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageFranchiseChannel.id) + "/" + str(franchiseID.id) + ")"
                #print("Test String: " + testString + " (" + str(len(testString)) + ")")
                
                embed = discord.Embed(title="Match #" + str(matchNum + 1) + ": " + franchiseInfo[0],description=testString)

                
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
                            replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0]
                        else:
                            if charactersReasonSubbing[protagonist][0] == "No Change":
                                replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") " + subVersion + " doesn't change."
                            else:
                                if charactersReasonSubbing[protagonist][0] == "Ages":
                                    if charactersReasonSubbing[protagonist][1].split("|")[1] == "1":
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0][0:len(charactersReasonSubbing[protagonist][1].split("|")[0])-1:] + ")"
                                    else:
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0] + ")"
                                else:
                                    replacementText = "[" + people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
                        
                        if len(replacementLines) + len(replacementText) >= 1024:
                            replacementList.append(replacementLines)
                            replacementLines = ""
                        replacementLines = replacementLines + "-" + replacementText + "\n"
                    except:
                        if charactersReasonSubbing[protagonist][0] == "Full Random":
                            replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0]
                        else:
                            if charactersReasonSubbing[protagonist][0] == "No Change":
                                replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ")" + subVersion + " doesn't change."
                            else:
                                if charactersReasonSubbing[protagonist][0] == "Ages":
                                    if charactersReasonSubbing[protagonist][1].split("|")[1] == "1":
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0][0:len(charactersReasonSubbing[protagonist][1].split("|")[0])-1:] + ")"
                                    else:
                                        replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1].split("|")[1] + " " + charactersReasonSubbing[protagonist][1].split("|")[0] + ")"
                                else:
                                    replacementText = "[" +  people[protagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origCharacters[protagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subCharacters[subCharacter].id) + ") " + subVersion + additive + "via " + charactersReasonSubbing[protagonist][0] + " (" + charactersReasonSubbing[protagonist][1] + ")"
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
                                replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0]
                            else:
                                if antagonistsReasonSubbing[antagonist][0] == "No Change":
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") " + subVersion + " doesn't change."
                                else:
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1] + ")"
                        except:
                            if antagonistsReasonSubbing[antagonist][0] == "Full Random":
                                replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0]
                            else:
                                if antagonistsReasonSubbing[antagonist][0] == "No Change":
                                    replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") " + subVersion + " doesn't change."
                                else:
                                    if antagonistsReasonSubbing[antagonist][0] == "Ages":
                                        if antagonistsReasonSubbing[antagonist][1].split("|")[1] == "1":
                                            replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1].split("|")[1] + " " + antagonistsReasonSubbing[antagonist][1].split("|")[0][0:len(antagonistsReasonSubbing[antagonist][1].split("|")[0])-1:] + ")"
                                        else:
                                            replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1].split("|")[1] + " " + antagonistsReasonSubbing[antagonist][1].split("|")[0] + ")"
                                    else:
                                        replacementText = "[" + people[antagonist][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(origAntags[antagonist].id) + ") is replaced by [" + people[subCharacter][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subAntags[subCharacter].id) + ") " + subVersion + additive + "via " + antagonistsReasonSubbing[antagonist][0] + " (" + antagonistsReasonSubbing[antagonist][1] + ")"
                        
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
                                replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0]
                            else:
                                if minionReplaceReasons[minion][0] == "No Change":
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") didn't change."
                                else:
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + adjective[:1:].capitalize() + adjective[1::] + "](" + "https://discord.com/channels/" + str(guildID) + "/" + str(messageAdjectivesChannel.id) + "/" + str(adjectives[adjective].id) + ")[" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")"
                        except:
                            if minionReplaceReasons[minion][0] == "Full Random":
                                print("[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ")")
                                print(minions[minionReplacements[minion]][0])
                                print(minion + ": ")
                                print(str(minionReplacements))
                                print(str(subMinions))
                                print(str(minionReplacements[minion]))
                                print("is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ")")
                                print("via " + minionReplaceReasons[minion][0])
                                replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0]
                            else:
                                if minionReplaceReasons[minion][0] == "No Change":
                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") didn't change."
                                else:
                                    print("[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ")")
                                    print(minions[minionReplacements[minion]][0])
                                    print(minion + ": ")
                                    print(str(minionReplacements))
                                    print(str(subMinions))
                                    print(str(minionReplacements[minion]))
                                    print(str(subMinions[minionReplacements[minion]].id))
                                    print("is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ")")
                                    print("via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")")

                                    replacementText = "[" + minions[minion][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messageMinionsChannel.id) + "/" + str(origMinions[minion].id) + ") is replaced by [" + minions[minionReplacements[minion]][0] + "](https://discord.com/channels/" + str(guildID) + "/" + str(messagePeopleChannel.id) + "/" + str(subMinions[minionReplacements[minion]].id) + ") via " + minionReplaceReasons[minion][0] + " (" + minionReplaceReasons[minion][1] + ")"
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
        
    await client.close()


    

client.run(trueToken)