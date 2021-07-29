numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import discord 

def infoCard(personName):
    firstChar = personName[0:1:]
    print("Opening path to " + personName + ": Characters\\" + firstChar + "\\" + personName + ".txt")
    personFile = open("Characters\\" + firstChar + "\\" + personName + ".txt", "r", encoding='utf8')
    personInfo = personFile.read().split("\n")

    embed = discord.Embed(title="Test", description="Test :)")

    if personInfo[2] != "":
        embed = discord.Embed(title=personInfo[0], description=personInfo[2][0:250:] + "...")
    else:
        embed = discord.Embed(title=personInfo[0])

    if personInfo[20] != "":    
        embed.add_field(name="Franchise",value=personInfo[20], inline=False)
    
    if personInfo[7] != "":
        actorString = ""
        for actor in personInfo[7].split("|"):
            actorString = actorString + actor + ", "
        actorString = actorString[0:len(actorString)-2:]
        embed.add_field(name="Actors", value=actorString, inline=False)

    if personInfo[9] != "":
        embed.add_field(name="Type",value=personInfo[9])
    if personInfo[10] != "":
        embed.add_field(name="Race",value=personInfo[10])
    if personInfo[13] != "":
        embed.add_field(name="Gender",value=personInfo[13])

    if personInfo[11] != "":
        embed.add_field(name="Alignment",value=personInfo[11], inline=True)
    #if personInfo[12] != "":
        #embed.add_field(name="Importance",value=personInfo[12], inline=False)
    if personInfo[15] != "":
        embed.add_field(name="Power Level",value=personInfo[15], inline=True)

    if personInfo[16] != "":
        embed.add_field(name="Fame",value=personInfo[16], inline=True)

    if personInfo[14] != "":
        tagString = ""
        for tag in personInfo[14].split(","):
            if len(tag.split("|")) >= 2:
                tagString = tagString + tag.split("|")[0] + " (" + tag.split("|")[1] + "), "
            else:
                tagString = tagString + tag + ", "
        tagString = tagString[0:len(tagString)-2:]
        embed.add_field(name="Tags",value=tagString, inline=False)

    if personInfo[17] != "":
        groupString = ""
        for group in personInfo[17].split(","):
            groupString = groupString + group + ", "
        groupString = groupString[0:len(groupString)-2:]
        embed.add_field(name="Groups", value=groupString, inline=False)

    if personInfo[21] != "":
        weaponString = ""
        for weapon in personInfo[21].split("|"):
            weaponString = weaponString + weapon + ", "
        weaponString = weaponString[0:len(weaponString)-2:]
        embed.add_field(name="Signature Weapon", value=weaponString, inline=False)
        
    if personInfo[18] != "":
        themeSong = "Megalovania|https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=a9791693d4f04223"
        if personInfo[18].split(",") >= 2:
            themeSongList = personInfo[18].split(",")
            RNG = random.randint(0,len(themeSongList)-1)
            themeSong = themeSongList[RNG]
        embed.add_field(name="Theme Song",value="[" + themeSong.split("|")[0] + "](" + themeSong.split("|")[1] + ")")


    if personInfo[3] != "":
        embed.set_thumbnail(url=personInfo[3])

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed