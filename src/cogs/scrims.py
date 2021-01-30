import json
import discord
from discord.ext import commands
import os

os.chdir("cogs")

async def get_data():
    with open("scrims.json" , "r") as f:
        scrims = json.load(f)

    return scrims

async def open_scrim(id , ownid , name ,description):
    scrims = await get_data()

    if name in scrims:
        return False

    else:
        scrims[id] = {}
        scrims[id]["name"] = name
        scrims[id]["description"] = description
        scrims[id]["status"] = "Participation"
        scrims[id]["prize"] = "none"
        scrims[id]["owner"] = ownid

        with open("scrims.json" , "w") as f:
            json.dump(scrims , f)

        return True

class Scrims(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command(aliases=["cs"])
    async def createscrim(self , ctx , name , * , description):
        await open_scrim(ctx.message.id , ctx.author.id , name , description)
        await ctx.send(f"Scrim Created by id {ctx.message.id}.")
        em = discord.Embed(title = "Scrim Created" , color = discord.Color.green())
        em.add_field(name = "Name" , value = name , inline = False)
        em.add_field(name = "Description" , value = description , inline = False)
        em.add_field(name = "ID" , value = ctx.message.id , inline = False)
        em.add_field(name = "Status" , value = "Participation" , inline = False)
        em.add_field(name = "Owner" , value = ctx.author.mention , inline = False)
        await ctx.send(embed = em)
        
    @commands.command()
    async def close(self , ctx , id):
        scrims = await get_data()
        a = scrims[id]["owner"]

        if a == ctx.author.id:
            scrims[id]["status"] = "Ongoing / Closed"

            with open("scrims.json" , "w") as f:
                json.dump(scrims , f)

            await ctx.send("Closed Participations for Scrim [id = {}]".format(id))

        else:
            await ctx.send("You are not the organizer of the scrim!")


    @commands.command()
    async def prize(self , ctx , id , * , prize):
        scrims = await get_data()
        a = scrims[id]["owner"]

        if a == ctx.author.id:
            scrims[id]["prize"] = prize

            with open("scrims.json" , "w") as f:
                json.dump(scrims , f)

            await ctx.send("Prize for Scrim [id = `{}`] is `{}`.".format(id , prize))

        else:
            await ctx.send("You are not the organizer of the scrim")

    @commands.command()
    async def scrim(self , ctx , id):
        scrims = await get_data()

        name = scrims[id]["name"]
        desc = scrims[id]["description"]
        status = scrims[id]["status"]
        prize = scrims[id]["prize"]
        ownid = scrims[id]["owner"]

        user = self.bot.get_user(ownid)

        em = discord.Embed(title = f"{name}" , description = desc , color = discord.Colour.blurple())
        em.add_field(name="Status" , value = status)
        em.add_field(name = "Prize" , value = prize)
        em.add_field(name="Organized By" , value = user.mention)
        em.set_footer(text="For more info contact the scrim organizer")

        await ctx.send(embed = em)


    @commands.command()
    async def rename(self , ctx , id , * , name):
        scrims = await get_data()
        a = scrims[id]["owner"]

        if a == ctx.author.id:
            scrims[id]["name"] = name

            with open("scrims.json" , "w") as f:
                json.dump(scrims , f)

            await ctx.send("Name for Scrim [id = `{}`] is `{}`.".format(id , name))

        else:
            await ctx.send("You are not the organizer of the scrim")

    @commands.command()
    async def description(self , ctx , id , * , description):
        scrims = await get_data()
        a = scrims[id]["owner"]

        if a == ctx.author.id:
        
            scrims[id]["description"] = description

            with open("scrims.json" , "w") as f:
                json.dump(scrims , f)

            await ctx.send("Description for Scrim [id = `{}`] is `{}`.".format(id , description))

        else:
           await ctx.send("You are not the organizer of the scrim.")

    @commands.command()
    async def scrims(self , ctx):
        scrims = await get_data()

        em = discord.Embed(title = "Available Scrims" , color = discord.Color.green())

        for i in scrims:
            status = scrims[i]["status"]
            if status == "Participation":
                a = scrims[i]["name"]
                b = scrims[i]["description"]
                c = scrims[i]["prize"]
                d = self.bot.get_user(scrims[i]["owner"])
                id = i

                em.add_field(name=a , value=f"Organized by - {d.mention}\nDescription - {b}\nPrize - {c}\nID - {id}")

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Scrims(bot))