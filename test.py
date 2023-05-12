import discord
import get_local_time as glt

TOKEN = "MTEwNTczNjg3MDExOTM1MDMxMw.GT1F4o.3DQwvjSnLzAWHaj7omHpzeqIihV_iLYH_AJ3NU"


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "i love who?":
            await message.channel.send("you love leann :)")


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
