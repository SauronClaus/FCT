# Generates the info embeds. 

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
        if personInfo[4] != "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Icon-round-Question_mark.svg/1200px-Icon-round-Question_mark.svg.png":
            embed = discord.Embed(title=personInfo[0], description=personInfo[2][0:650:] + "[. . .](" + personInfo[4] + ")")
        else:
            embed = discord.Embed(title=personInfo[0], description=personInfo[2][0:1024:])
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
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")", inline=False)


    if personInfo[3] != "":
        embed.set_thumbnail(url=personInfo[3])

    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")
    if len(personInfo) == 29:
        if personInfo[26] != "" and personInfo[26] != "Sebastian":
            contributorsString = ""
            contributors = personInfo[26].split(",")
            if len(contributors) > 2:
                x = 0
                print("Length: " + str(len(contributors)))
                for author in contributors:
                    if x < len(contributors)-1:
                        contributorsString = contributorsString + author + ", "
                        x+=1
                        print("X: " + str(x))
                contributorsString = contributorsString[0:len(contributorsString)-1:]
            else:
                if len(contributors) == 2:
                    contributorsString = contributors[0]
                    x = 1
                else:
                    x=0
            if len(contributors) > 1:
                contributorsString = contributorsString + " and " + contributors[x]
            else:
                contributorsString = contributors[x]
            embed.set_footer(text="Created by The Invisible Man, with help from " + contributorsString, icon_url="https://i.imgur.com/tce0LOa.jpg")
        else:
            embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
        if personInfo[28] != "" and personInfo[28] != "No":
            personInfoTest = personInfo[28].split("|")
            if len(personInfoTest) > 1:
                if personInfoTest[0] == "Guild Only":
                    embed.add_field(name="Restrictions", value="Restricted to guild: " + personInfoTest[1], inline=False)
            if personInfo[28] == "No Sub In":
                embed.add_field(name="Restrictions", value="No Substituting In",inline=False)
            
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

    embed.color = colors[franchiseInfo[15]]
    print("Starting Individual Fields.")
    if franchiseInfo[12] != "":
        embed.add_field(name="Franchise",value=franchiseInfo[12], inline=False)
        print("Franchise: " + franchiseInfo[12])

    if franchiseInfo[14] != "":
        mediumString = ""
        for medium in franchiseInfo[14].split(","):
            mediumString = mediumString + medium + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        embed.add_field(name="Mediums",value=mediumString, inline=True)
        print("Mediums: " + franchiseInfo[14])

    if franchiseInfo[17] != "":
        embed.add_field(name="Average Power Level",value=franchiseInfo[17], inline=True)
        print("Average Power Level: " + franchiseInfo[17])

    if franchiseInfo[7] != "":
        characterInsertsString = ""
        for character in franchiseInfo[7].split("|"):
            characterInsertsString = characterInsertsString + character + ", "
        characterInsertsString = characterInsertsString[0:len(characterInsertsString)-2:]
        embed.add_field(name="Character Inserts",value=characterInsertsString, inline=False)
        print("Character Inserts: " + characterInsertsString)

    if franchiseInfo[8] != "":
        characterInsertsString = ""
        for character in franchiseInfo[8].split("|"):
            characterInsertsString = characterInsertsString + character + ", "
        characterInsertsString = characterInsertsString[0:len(characterInsertsString)-2:]
        embed.add_field(name="Antagonist Inserts",value=characterInsertsString, inline=False)
        print("Antagonist Inserts: " + characterInsertsString)



    if franchiseInfo[11] != "":
        themeSong = "Megalovania|https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=a9791693d4f04223"
        if len(franchiseInfo[11].split("|")) >= 2:
            themeSongList = franchiseInfo[11].split(",")
            RNG = random.randint(0,len(themeSongList)-1)
            themeSong = themeSongList[RNG]
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")")
        print("Theme Song: " + themeSong.split("|")[0])
    if franchiseInfo[4] != "":
        goalsString = ""
        for goal in franchiseInfo[4].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Normal Goals",value=goalsString, inline=False)
        print("Normal Goals: " + goalsString)
    
    if franchiseInfo[5] != "":
        goalsString = ""
        for goal in franchiseInfo[5].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Stretch Goals",value=goalsString, inline=False)
        print("Stretch Goals: " + goalsString)
    
    if franchiseInfo[6] != "":
        goalsString = ""
        for goal in franchiseInfo[6].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Reach Goals",value=goalsString, inline=False)
        print("Reach Goals: " + goalsString)

    
    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    if franchiseInfo[18] != "" and franchiseInfo[18] != "Sebastian":
        contributorsString = ""
        contributors = franchiseInfo[18].split(",")
        if len(contributors) > 2:
            x = 0
            print("Length: " + str(len(contributors)))
            for author in contributors:
                if x < len(contributors)-1:
                    contributorsString = contributorsString + author + ", "
                    x+=1
                    print("X: " + str(x))
            contributorsString = contributorsString[0:len(contributorsString)-1:]
        else:
            contributorsString = contributors[0]
            x = 1
        contributorsString = contributorsString + " and " + contributors[x]
        embed.set_footer(text="Created by The Invisible Man, with help from " + contributorsString, icon_url="https://i.imgur.com/tce0LOa.jpg")
    else:
        embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed

def infoAdjective(adjective, fctPolls):
    print("Adjective: " + adjective)
    if adjective[len(adjective)-1::] != "-" and adjective[len(adjective)-1::] != " ":
        adjective = adjective + " "
    if adjective[len(adjective)-1::] != "-":
        contentFile = open("Adjectives\\Descriptions\\" + adjective[:len(adjective)-1:] + ".txt", "r")
    else:
        contentFile = open("Adjectives\\Descriptions\\" + adjective + ".txt", "r")
        
    contentFull = contentFile.read()
    content = contentFull.split("\n")

    embed = discord.Embed(title=adjective[:1:].capitalize() + adjective[1::], description=content[0].capitalize()[:1:] + content[0][1::], color=0xFF9900)

    if not(content[1].startswith("https://www.dictionary.com/")):
        embed.add_field(name="Link",value=content[1], inline=False)
    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    
    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")
    
    return embed

def infoMinions(minionName, fctPolls):
    print("Opening path to " + minionName + ": Minions\\" + minionName + ".txt")
    minionsFile = open("Minions\\" + minionName + ".txt", "r", encoding='utf8')
    minionsInfo = minionsFile.read().split("\n")


    embed = discord.Embed(title="Test", description="Test :)")

    if minionsInfo[2] != "":
        embed = discord.Embed(title=minionsInfo[0], description=minionsInfo[2][0:250:] + "[. . .](" + minionsInfo[4] + ")")
    else:
        embed = discord.Embed(title=minionsInfo[0])
    
    if minionsInfo[3] != "":
        embed.set_thumbnail(url=minionsInfo[3])

    embed.color = colors[minionsInfo[18]]
    
    if minionsInfo[1] != "":
        embed.add_field(name="Franchise",value=minionsInfo[1], inline=False)

    if minionsInfo[16] != "":
        mediumString = ""
        for medium in minionsInfo[16].split(","):
            mediumString = mediumString + medium + ", "
        mediumString = mediumString[0:len(mediumString)-2:]
        embed.add_field(name="Mediums",value=mediumString, inline=True)

    if minionsInfo[13] != "":
        embed.add_field(name="Average Power Level",value=minionsInfo[13], inline=True)

    if minionsInfo[11] != "":
        embed.add_field(name="Alignment",value=minionsInfo[11], inline=True)

    if minionsInfo[10] != "":
        embed.add_field(name="Race",value=minionsInfo[10], inline=True)
    
    if minionsInfo[9] != "":
        embed.add_field(name="Type",value=minionsInfo[9], inline=True)
    
    if minionsInfo[14] != "":
        embed.add_field(name="Popularity",value=minionsInfo[9], inline=True)

    if minionsInfo[19] != "":
        minionsPowerString = ""
        for powerSet in minionsInfo[19].split(","):
            powersInfo = powerSet.split("|")
            minionsPowerString = minionsPowerString + powersInfo[0] + " (" + powersInfo[1] + "): Tier " + str(powersInfo[2]) + ", "
        minionsPowerString = minionsPowerString[0:len(minionsPowerString)-2:]
        embed.add_field(name="Powers",value=minionsPowerString, inline=False)

    if minionsInfo[15] != "":
        themeSong = "Megalovania|https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=a9791693d4f04223"
        if len(minionsInfo[15].split("|")) >= 2:
            themeSongList = minionsInfo[15].split(",")
            RNG = random.randint(0,len(themeSongList)-1)
            themeSong = themeSongList[RNG]
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")")
    
    if minionsInfo[5] != "":
        goalsString = ""
        for goal in minionsInfo[5].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Commanders",value=goalsString, inline=False)
    
    if minionsInfo[6] != "":
        goalsString = ""
        for goal in minionsInfo[6].split("|"):
            goalsString = goalsString + goal + ", "
        goalsString = goalsString[0:len(goalsString)-2:]
        embed.add_field(name="Associated Groups",value=goalsString, inline=False)
    
    if fctPolls != "":
        embed.add_field(name="Return to Poll",value="[Here](" + "https://discord.com/channels/" + str(fctPolls.guild.id) + "/" + str(fctPolls.id) + ")")

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed