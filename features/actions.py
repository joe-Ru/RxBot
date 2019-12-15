import requests


# *** These commands below are for whenever a user joins the server ***
# *** They are not printed out on the server itself ***
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

# Finds the ping of the user
@client.command()
async def ping(ctx): #ctx means context
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

def getCatPicture():
    catPicture = requests.get('http://thecatapi.com/api/images/get.php')
    if catPicture.status_code == 200:
        catPicture = catPicture.url
        return catPicture

    else:
        return 'Error 404. Website may be down.'