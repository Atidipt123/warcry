import discord
from discord.ext import commands
import random
import asyncio
import json

bot = commands.Bot(command_prefix='$' , intents = discord.Intents.all())
token = 'ur bot token'

bot.load_extension("cogs.info")
bot.load_extension("cogs.utilities")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.scrims")
bot.load_extension("cogs.modmail")
bot.load_extension("cogs.image")
bot.load_extension("cogs.tags")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

async def chs():
    await bot.wait_until_ready()

    statuses = ['Call of Duty Mobile | $help' , 'Moderating WarCry Server | $help' , 'https://www.instagram.com/warcryofficial/ | $help' , 'https://twitter.com/warcrycodm | $help']
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity = discord.Game(status))
        await asyncio.sleep(10)

@bot.event
async def on_member_join(member: discord.Member):
    chnl = await bot.fetch_channel(724878406331793478)
    await chnl.send(f"Welcome {member.mention}.\nIf u want to join WarCry go to <#755393138864029776> and type '/apply' then a bot will dm you the form . You need to fill it. And also follow us on social media , links in <#800083471082455080>  or use command $social")

@bot.event
async def on_member_remove(member: discord.Member):
    chnl = await bot.fetch_channel(728462027135254618)
    await chnl.send(f"**__{member.name}#{member.discriminator}**__ Left the server!")


@bot.event
async def on_command_error(ctx , error):
    await ctx.send(f":negative_squared_cross_mark: {error}")

bot.loop.create_task(chs())
bot.run(token)