numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import discord
import random
from colors import colors


def infoPerson(personName, fctPolls):
    firstChar = personName[0:1:]
    if firstChar in numbers:
        firstChar = "#"
    print("Opening path to " + personName + ": Characters\\" + firstChar + "\\" + personName + ".txt")
    personFile = open("Characters\\" + firstChar + "\\" + personName + ".txt", "r", encoding='utf8')
    personInfo = personFile.read().split("\n")


    embed = discord.Embed(title="Test", description="Test :)")

    if personInfo[2] != "":
        #print(str(len(personInfo[2])) + ", truncated to " + str(len(personInfo[2][0:250:])))
        embed = discord.Embed(title=personInfo[0], description=personInfo[2][0:250:] + "[. . .](" + personInfo[4] + ")")
    else:
        embed = discord.Embed(title=personInfo[0])

    embed.color = colors[personInfo[23]]

    if personInfo[21] != "":    
        embed.add_field(name="Franchise",value=personInfo[21], inline=False)
    

    if personInfo[8] != "":
        actorString = ""
        for actor in personInfo[8].split("|"):
            actorString = actorString + actor + ", "
        actorString = actorString[0:len(actorString)-2:]
        embed.add_field(name="Actors", value=actorString, inline=False)

    if personInfo[10] != "":
        embed.add_field(name="Type",value=personInfo[10])
    if personInfo[11] != "":
        embed.add_field(name="Race",value=personInfo[11])
    if personInfo[14] != "":
        embed.add_field(name="Gender",value=personInfo[14])

    if personInfo[12] != "":
        embed.add_field(name="Alignment",value=personInfo[12], inline=True)
    #if personInfo[13] != "":
        #embed.add_field(name="Importance",value=personInfo[13], inline=False)
    if personInfo[16] != "":
        embed.add_field(name="Power Level",value=personInfo[16], inline=True)

    if personInfo[17] != "":
        embed.add_field(name="Fame",value=personInfo[17], inline=True)

    if personInfo[15] != "":
        tagString = ""
        for tag in personInfo[15].split(","):
            if len(tag.split("|")) >= 2:
                tagString = tagString + tag.split("|")[0] + " (" + tag.split("|")[1] + "), "
            else:
                tagString = tagString + tag + ", "
        tagString = tagString[0:len(tagString)-2:]
        embed.add_field(name="Tags",value=tagString, inline=False)

    if personInfo[18] != "":
        groupString = ""
        for group in personInfo[18].split(","):
            groupString = groupString + group + ", "
        groupString = groupString[0:len(groupString)-2:]
        embed.add_field(name="Groups", value=groupString, inline=False)

    if personInfo[22] != "":
        weaponString = ""
        for weapon in personInfo[22].split("|"):
            weaponString = weaponString + weapon + ", "
        weaponString = weaponString[0:len(weaponString)-2:]
        embed.add_field(name="Signature Weapon", value=weaponString, inline=False)
        
    if personInfo[19] != "":
        themeSong = "Megalovania|https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=a9791693d4f04223"
        if len(personInfo[19].split("|")) >= 2:
            themeSongList = personInfo[19].split(",")
            RNG = random.randint(0,len(themeSongList)-1)
            themeSong = themeSongList[RNG]
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")")


    if personInfo[3] != "":
        embed.set_thumbnail(url=personInfo[3])

    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed

def infoArtifact(artifactName, fctPolls):
    print("Opening path to " + artifactName + ": Artifacts\\" + artifactName + ".txt")
    artifactFile = open("Artifacts\\" + artifactName + ".txt", "r", encoding='utf8')
    artifactInfo = artifactFile.read().split("\n")

    embed = discord.Embed(title="Test", description="Test :)")

    if artifactInfo[2] != "":
        embed = discord.Embed(title=artifactInfo[0], description=artifactInfo[2][0:250:] + "[. . .](" + artifactInfo[4] + ")")
    else:
        embed = discord.Embed(title=artifactInfo[0])

    embed.color = colors[artifactInfo[13]]
    if artifactInfo[3] != "":
        embed.set_thumbnail(url=artifactInfo[3])

    if artifactInfo[5] != "":
        embed.add_field(name="Franchise",value=artifactInfo[5], inline=False)

    if artifactInfo[8] != "":
        mediumString = ""
        for medium in artifactInfo[8].split(","):
            mediumString = mediumString + medium + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        embed.add_field(name="Medium",value=mediumString, inline=True)

    if artifactInfo[9] != "":
        artifactThing = artifactInfo[9].split("|")
        embed.add_field(name="Type",value=artifactThing[0] + ": " + artifactThing[1], inline=True)
    if artifactInfo[11] != "":
        embed.add_field(name="Power Level",value=artifactInfo[11], inline=True)

    if artifactInfo[7] != "":
        tagString = ""
        for tag in artifactInfo[7].split(","):
            if len(tag.split("|")) >= 2:
                tagString = tagString + tag.split("|")[0] + " (" + tag.split("|")[1] + "), "
            else:
                tagString = tagString + tag + ", "
        tagString = tagString[0:len(tagString)-2:]
        embed.add_field(name="Tags",value=tagString, inline=False)

    if artifactInfo[6] != "":
        wielderString = ""
        for person in artifactInfo[6].split("|"):
            wielderString = wielderString + person + ", "
        wielderString = wielderString[0:len(wielderString)-2:]
        embed.add_field(name="Wielders",value=wielderString, inline=False)
    if artifactInfo[10] != "":
        artifactSetString = ""
        for artifactSet in artifactInfo[10].split("|"):
            artifactSetString = artifactSetString + artifactSet + ", "
        artifactSetString = artifactSetString[0:len(artifactSetString)-2:]
        embed.add_field(name="Sets",value=artifactSetString, inline=False)

    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed

def infoFranchise(franchiseName, fctPolls):
    firstChar = franchiseName[0:1:]
    if firstChar in numbers:
        firstChar = "#"
    print("Opening path to " + franchiseName + ": Franchises\\" + firstChar + "\\" + franchiseName + ".txt")
    franchiseFile = open("Franchises\\" + firstChar + "\\" + franchiseName + ".txt", "r", encoding='utf8')
    franchiseInfo = franchiseFile.read().split("\n")


    embed = discord.Embed(title="Test", description="Test :)")

    if franchiseInfo[1] != "":
        embed = discord.Embed(title=franchiseInfo[0], description=franchiseInfo[1][0:250:] + "[. . .](" + franchiseInfo[3] + ")")
    else:
        embed = discord.Embed(title=franchiseInfo[0])
    
    if franchiseInfo[2] != "":
        embed.set_thumbnail(url=franchiseInfo[2])

    embed.color = colors[franchiseInfo[14]]
    
    if franchiseInfo[11] != "":
        embed.add_field(name="Franchise",value=franchiseInfo[11], inline=False)

    if franchiseInfo[12] != "":
        mediumString = ""
        for medium in franchiseInfo[12].split(","):
            mediumString = mediumString + medium + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        embed.add_field(name="Mediums",value=mediumString, inline=True)

    if franchiseInfo[15] != "":
        embed.add_field(name="Average Power Level",value=franchiseInfo[15], inline=True)

    if franchiseInfo[7] != "":
        characterInsertsString = ""
        for character in franchiseInfo[7].split("|"):
            characterInsertsString = characterInsertsString + character + ", "
        characterInsertsString = characterInsertsString[0:len(characterInsertsString)-2:]
        embed.add_field(name="Character Inserts",value=characterInsertsString, inline=False)

    if franchiseInfo[8] != "":
        characterInsertsString = ""
        for character in franchiseInfo[8].split("|"):
            characterInsertsString = characterInsertsString + character + ", "
        characterInsertsString = characterInsertsString[0:len(characterInsertsString)-2:]
        embed.add_field(name="Antagonist Inserts",value=characterInsertsString, inline=False)


    if franchiseInfo[10] != "":
        themeSong = "Megalovania|https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=a9791693d4f04223"
        if len(franchiseInfo[10].split("|")) >= 2:
            themeSongList = franchiseInfo[10].split(",")
            RNG = random.randint(0,len(themeSongList)-1)
            themeSong = themeSongList[RNG]
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")")

    if franchiseInfo[4] != "":
        goalsString = ""
        for goal in franchiseInfo[4].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Normal Goals",value=goalsString, inline=False)
    
    if franchiseInfo[5] != "":
        goalsString = ""
        for goal in franchiseInfo[5].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Stretch Goals",value=goalsString, inline=False)
    
    if franchiseInfo[6] != "":
        goalsString = ""
        for goal in franchiseInfo[6].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Reach Goals",value=goalsString, inline=False)
    
    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed

def infoAdjective(adjective):
    print("Adjective: " + adjective)
    if adjective[len(adjective)-1::] != "-":
        contentFile = open("Adjectives\\Descriptions\\" + adjective[:len(adjective)-1:] + ".txt", "r")
    else:
        contentFile = open("Adjectives\\Descriptions\\" + adjective + ".txt", "r")
    
    contentFull = contentFile.read()
    content = contentFull.split("\n")

    embed = discord.Embed(title=adjective[:1:].capitalize() + adjective[1::], description=content[0].capitalize()[:1:] + content[0][1::], color=0xFF9900)

    if not(content[1].startswith("https://www.dictionary.com/")):
        embed.add_field(name="Link",value=content[1], inline=False)
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    return embed