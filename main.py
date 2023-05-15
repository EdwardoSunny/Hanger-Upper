import discord
import datetime as dt
from datetime import datetime, timezone
from discord.ext import commands
import get_local_time as glt
import pytz
import asyncio

utc = dt.timezone.utc

#timezone conversions from utc
def timetz_to_tz(t, tz_out):
    return datetime.combine(datetime.today(), t).astimezone(tz_out).timetz()

def timetz_to_tz_naive(t, tz_out):
    return datetime.combine(datetime.today(), t).astimezone(tz_out).time()

def time_to_tz(t, tz_out):
    return tz_out.localize(datetime.combine(datetime.today(), t)).timetz()

def time_to_tz_naive(t, tz_in, tz_out):
    return tz_in.localize(datetime.combine(datetime.today(), t)).astimezone(tz_out).time()

# in UTC timezone by default, but I'm giving LAX time
ht = dt.time(5,50,4) # 5:50 AM LAX time
# convert to back to UTC timezone for comparision (reverse timezones to convert back and forth)
ht = time_to_tz_naive(ht, pytz.timezone('America/Los_Angeles'), pytz.utc) # Boston timezone is: America/New_York
ht_city = "LAX"
TOKEN = "MTEwNTczNjg3MDExOTM1MDMxMw.GT1F4o.3DQwvjSnLzAWHaj7omHpzeqIihV_iLYH_AJ3NU"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# kick all from vc
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def hangupall(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.move_to(None)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def ptht(ctx):
    global ht, ht_city
    # convert back to LAX or BOS so can read/understand
    temp_ht = ht
    if (ht_city == "LAX"):
        temp_ht = time_to_tz_naive(temp_ht, pytz.utc, pytz.timezone('America/Los_Angeles'))
    else:
        temp_ht = time_to_tz_naive(temp_ht, pytz.utc, pytz.timezone('America/New_York'))
    await ctx.send("Set to hang up at: " + str(temp_ht) + ", " + ht_city + " time")

# 0155b --> 1:55 BOS
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def hangtime(ctx, arg):
    # modify outside vars dum py moment
    global ht, ht_city
    # in UTC right now
    time = arg[0:len(arg)-1]
    # glt only takes upper case
    ht_city = arg[-1].upper()
    if (time.isnumeric() and len(time) == 4):
        # default UTC
        ht = dt.time(int(time[0:2]), int(time[2:4]), 0)
        if (ht_city == "L"):
            ht_city = "BOS"
        else:
            ht_city = "LAX"
        await ctx.send("I will hang up at: " + str(ht) + ", " + str(ht_city) + " time")
        # convert back to UTC bc overall hang up comparison will be in UTC
        if (ht_city == "BOS"):
            ht = time_to_tz_naive(ht, pytz.timezone('America/New_York'), pytz.utc)
        else:
            ht = time_to_tz_naive(ht, pytz.timezone('America/Los_Angeles'), pytz.utc)
    else:
        await ctx.send("ERROR: incorrect date time format, please format with HHMMl or HHMMe")
    # current_time = glt.get_time_from_key(city)
    while True:
        print("running")
        try:
            await asyncio.sleep(5)
            # print(ht)
            # print(dt.datetime.now(timezone.utc))
            if (dt.datetime.now(timezone.utc).hour == ht.hour) and (dt.datetime.now(timezone.utc).minute == ht.minute):
                command = bot.get_command('hangupall')
                await command(ctx)
                # await ctx.send("Kicking everyone now")
                break
        except:
            print("ERROR: something happened while looping check time")
            break

bot.load_extension('time_cog')
bot.run(TOKEN)
