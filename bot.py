import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.') #This is the prefix to command the bot


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
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, * , question):
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


client.run('NjU1MjExMjY0MjAwNDA5MDkw.XfQ17g.bST_82pKnbZSZnTe24jZ-WAFsNA') #This is the bot token inside
    
   