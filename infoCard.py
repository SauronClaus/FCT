numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

import discord 

def infoCard(personName):
    firstChar = personName[0:1:]
    print("Opening path to " + personName + ": Characters\\" + firstChar + "\\" + personName + ".txt")
    personFile = open("Characters\\" + firstChar + "\\" + personName + ".txt", "r", encoding='utf8')
    personInfo = personFile.read().split("\n")
    embed = discord.Embed(title=personInfo[0], description=personInfo[2])
        
    #embed.add_field(name="Further Information",value="[Here](" + self.infoLink + ")")
    embed.set_thumbnail(url=personInfo[3])

    embed.set_footer(text="Created by The Invisible Man", icon_url="https://i.imgur.com/tce0LOa.jpg")

    return embed