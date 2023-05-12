import discord
import get_local_time as glt

TOKEN = "MTEwNTczNjg3MDExOTM1MDMxMw.GT1F4o.3DQwvjSnLzAWHaj7omHpzeqIihV_iLYH_AJ3NU"


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(">hello"):
        await message.channel.send("Heyy! How's it hanging?")
    if message.content.lower() == ">la time":
        current_time = glt.get_time_from_key("LA")
        await message.channel.send("The time in Los Angeles, CA is " + current_time)
    if message.content.lower() == ">bos time":
        current_time = glt.get_time_from_key("BOS")
        await message.channel.send("The time in Boston, MA is " + current_time)


client.run(TOKEN)
