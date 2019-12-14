#TODO:
# 1) Place 8ball command in features folder
# 2) Use your own cat api to implement
# 3) 

import discord
import random
import requests
from discord.ext import commands


client = commands.Bot(command_prefix = '!') #This is the prefix to command the bot


@client.event
async def on_ready():
    print('RxBot is operational')

'''
*** These commands below are for whenever a user joins the server ***
*** They are not printed out on the server itself ***
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')
'''

@client.command()
async def ping(ctx): #ctx means context
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Pong! {round(client.latency * 1000)}')
    

# This awaits for the command 'clear" and the amount of messages to clear.
# If no amount is specified then the default amount it takes is 5, as shown below.

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


@client.event 
async def on_message(message):
    msgText = message.content.lower()
    if (msgText.startswith('hello') or msgText.startswith('hey') or msgText.startswith('hi')):
        print(f"Hello")

client.run('NjU1MjExMjY0MjAwNDA5MDkw.XfQ17g.bST_82pKnbZSZnTe24jZ-WAFsNA') #This is the bot token inside
    
   