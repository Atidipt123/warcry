import json
import os
import discord
from discord.ext import commands


async def get_data():
    with open("tags.json" , "r") as f:
        tags = json.load(f)

    return tags

async def tag(title , reply):
    tags = await get_data()

    if title in tags:
        return False

    else:
        tags[str(title)] = {}
        tags[str(title)]["reply"] = reply

    with open("tags.json" , "w") as f:
        json.dump(tags , f)

        return True

class Tags(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command(aliases=["nt"])
    @commands.has_permissions(manage_messages=True)
    async def newTag(self , ctx , title , * , reply):
        tags = await get_data()
        await tag(title , reply)
        await ctx.send("Tag Created!")

    @commands.command()
    async def tag(self , ctx , name):
        tags = await get_data()

        if name in tags:
            response = tags[name]["reply"]
            await ctx.send(response)

        else:
            await ctx.send(":negative_squared_cross_mark: Tag not found")

    @commands.command()
    async def tags(self , ctx):
        tags = await get_data()
        em = discord.Embed(title = "Tags")

        for i in tags:
            name = i
            em.add_field(name=name , value = "No Data")

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Tags(bot))