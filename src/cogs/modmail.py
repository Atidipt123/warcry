import discord
from discord.ext import commands
import json
import os

async def get_data():
    with open("modmail.json" , "r") as f:
        msgs = json.load(f)

    return msgs

async def open_query(msg):
    msgs = await get_data()

    if str(msg.id) in msgs:
        return False

    else:
        msgs[str(msg.id)] = {}
        msgs[str(msg.id)]["id"] = msg.author.id
        msgs[str(msg.id)]["query"] = msg.content
        msgs[str(msg.id)]["closed"] = "false"

    with open("modmail.json" , "w") as f:
        json.dump(msgs , f)

        return True

class Modmail(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self , msg: discord.Message):
        if msg.guild == None and msg.author!= self.bot.user:
            await open_query(msg)
            chnl = await self.bot.fetch_channel(728123564200427540)
            #chnl = await self.bot.fetch_channel(802192293686804502)
            em = discord.Embed(title="New DM Message" , description=f"**__{msg.author.name}#{msg.author.discriminator}__**\n{msg.content}")
            em.set_footer(text=f"Query ID - {msg.id}")

            await chnl.send(embed=em)
            await msg.channel.send("Message sent to the server succesfully!")

    @commands.command()
    async def reply(self , ctx , id , * , rmsg):
        msgs = await get_data()
        if msgs[str(id)]["closed"] == "false":
            uid = msgs[str(id)]["id"]
            user = self.bot.get_user(uid)
            await user.send(rmsg)
            await ctx.send("MESSAGE SENT")

        else:
            await ctx.send("Query is closed.")

    @commands.command()
    async def lock(self , ctx , msg):
        msgs = await get_data()
        if msgs[str(msg)]["closed"] == "false":
            msgs[str(msg)]["closed"] = "true"

            with open("modmail.json" , "w") as f:
                json.dump(msgs , f)

            await ctx.send("Closed")
            uid = msgs[str(id)]["id"]
            user = self.bot.get_user(uid)
            await user.send("Query Closed")

        else:
            await ctx.send("Query is already closed.")

def setup(bot):
    bot.add_cog(Modmail(bot))
