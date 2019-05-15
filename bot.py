import discord 
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")
autoModID = 471380698381680650



filterWords = []

#HASH TABLE OF ALL TWITCH CHANNELS
twitchChannels = {}
twitchChannels["OMAR"] = "https://www.twitch.tv/throwmar"
twitchChannels["THROWMAR"] = "https://www.twitch.tv/throwmar"
twitchChannels["GERRIT"] = "https://www.twitch.tv/froazentoast"
twitchChannels["FROAZENTOAST"] = "https://www.twitch.tv/froazentoast"
twitchChannels["MARK"] = "https://www.twitch.tv/geogebrush"
twitchChannels["GEOGEBRUSH"] = "https://www.twitch.tv/geogebrush"
twitchChannels["TYLER1"] = "https://www.twitch.tv/loltyler1"
twitchChannels["BRENDON"] = "https://www.twitch.tv/Slamgasm"
twitchChannels["SLAMGASM"] = "https://www.twitch.tv/Slamgasm"
twitchChannels["LUKE"] = "https://www.twitch.tv/WarlockShepard"
twitchChannels["WARLOCKSHEPARD"] = "https://www.twitch.tv/WarlockShepard"
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):

    if int(message.author.id) == autoModID:
        return

    if len(message.attachments) > 0:
        pics = discord.Embed()
        pics.set_image(url = message.attachments[0]['url'])
        await client.send_message(message.channel,embed=pics)
    

    if message.content.upper().startswith("!TWITCH") or message.content.upper().startswith("!T"):
        x = message.content.split()
        await client.send_message(message.channel, twitchChannels[x[1].upper()])


    for x in message.content.split():
        if x.upper() in filterWords:
            userID = message.author.id
            e = discord.Embed()
            e.set_image(url = "https://cdn.discordapp.com/attachments/471382715657224214/471840753925095427/image.jpg")
            await client.delete_message(message)
            await client.send_message(message.channel, embed=e)
            await client.send_message(message.channel, "<@%s>, please do not use that word in this server" % (userID))
            break

        if x.upper() == "BRENDAN":
            userID = message.author.id    
            await client.send_message(message.channel, "<@%s>, did you mean to spell \"brendon\"?" % (userID))
            break
    

@client.event
async def on_channel_update(before, after):
    if (before.bitrate != after.bitrate):
        await client.send_message(client.get_channel('471382715657224214'), 'bitrate was changed from ' + str(before.bitrate) + ' to ' + str(after.bitrate))




    
    






