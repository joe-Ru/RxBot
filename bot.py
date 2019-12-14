import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') #This is the prefix to command the bot

@client.event
async def on_ready():
    print('RxBot is operational')

client.run('NjU1MjExMjY0MjAwNDA5MDkw.XfQ17g.bST_82pKnbZSZnTe24jZ-WAFsNA') #This is the bot token inside
