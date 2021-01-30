import discord
from discord.ext import commands
from io import BytesIO
from PIL import Image , ImageFont , ImageDraw
import os


class Images(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command()
    async def punch(self ,ctx , * , member: discord.Member = None):
        if member == None:
            member = ctx.author

        punching = Image.open("assets/punch.png")
        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((133 , 118))
        punching.paste(pfp , (294 , 34))
        punching.save("assets/punched.png")

        await ctx.send(file = discord.File("assets/punched.png"))

    @commands.command()
    async def achievement(self , ctx , * , text):
        img = Image.open("assets/a.png")
        font = ImageFont.truetype("assets/Roboto-Regular.ttf" , 24)

        draw = ImageDraw.Draw(img)

        t = text
        draw.text((57 , 33) , t , (250 , 250 ,250) , font=font)
        img.save("assets/noice.png")

        await ctx.send(file=discord.File("assets/noice.png"))

    @commands.command()
    async def slap(self , ctx , * , member: discord.Member = None):
        if member == None:
            member = ctx.author

        slapping = Image.open("assets/slapped.jpg")
        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((133 , 118))
        slapping.paste(pfp , (109 , 42))
        slapping.save("assets/yo.jpg")

        await ctx.send(file = discord.File("assets/yo.jpg"))

def setup(bot):
    bot.add_cog(Images(bot))