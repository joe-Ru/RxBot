#TODO: Make bot post cat picture with API

import discord
import random
import requests
from features import *
from discord.ext import commands


# client = commands.Bot(command_prefix = '!') #This is the prefix to command the bot
client = discord.Client()

@client.event
async def on_ready():
    print('RxBot is operational')

'''
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    await ctx.channel.purge(limit=1)
    responses =  ["It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes - definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Below works, however not shown on the discord channel
@client.event 
async def on_message(message):
    msgText = message.content.lower()
    if (msgText.startswith('hello') or msgText.startswith('hey') or msgText.startswith('hi')):
        print(f"Hello")
'''
@client.event
async def on_message(message):
        # Random cat picture
        if message.content.startswith('shutdown') and message.author.id == config.OWNERID:
            await client.send_message(message.channel, 'Shutting down. Bye!')
            await client.logout()
            await client.close()

        elif message.content.startswith('cat'):
            await client.send_message(message.channel, actions.getCatPicture())


client.run('NjU1MjExMjY0MjAwNDA5MDkw.XfZA7A.bvM1bRqUW4vVCidMVisQ97cdVhA') #This is the bot token inside
    
   