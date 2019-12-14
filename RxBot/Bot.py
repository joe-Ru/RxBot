import discord


# server ID = 448822640811966464

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()


@client.event
async def on_message(message):
    id = client.get_guild(448822640811966464)  # place server token here
    channels = ["bot"]  # place the channels you would like the bot to function in only in there
    # Example "bot" for a channel named "bot"

    if str(message.channel) in channels:
        if message.content.find("+ping") != -1:  # if user messages ping, then do pong
            await message.channel.send("pong")

        elif message.content == "+users":
            await message.channel.send(f""" # of Members {id.member_count}""")

        # elif message.content == "+" +


client.run("NjQ4OTkyODczMjQ0Nzg2NzI5.Xd2tPw.pQiGnX2AVzYhIZuRAYw-I_LCIjE")
