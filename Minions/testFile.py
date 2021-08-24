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
            minionsPowerString = minionsPowerString + powerSet[0] + " (" + powerSet[1] + "): Tier " + str(powerSet[2]) + ", "
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