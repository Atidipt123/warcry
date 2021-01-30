import discord
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command()
    async def ping(self , ctx):
        p = round(self.bot.latency*1000)
        em = discord.Embed(title="Bot Latency" , description=f":green_circle: {p}ms" , color = discord.Color.green())
        await ctx.send(embed=em)

    @commands.command()
    async def avatar(self , ctx , user: discord.User = None):
        if user == None:
            user=ctx.author
        await ctx.send(f"__**{user.name}#{user.discriminator}**__'s Avatar\n{user.avatar_url}")

    @commands.command(aliases=["yt" , "youtube" , "insta" , "instagram" , "twitter"])
    async def social(self , ctx):
        em = discord.Embed(title="WarCry's Social Links" , color = discord.Color.blue())
        em.add_field(name = "Instagram" , value = "<:instalogo:802493294827274272> [Click Here](https://www.instagram.com/warcryofficial/)")
        em.add_field(name = "YouTube" , value = "<:ytlogo:802493272315396126> [Click Here](https://www.youtube.com/channel/UCexbjXlS_RC_0K9KmlSkN2Q/videos)")
        em.add_field(name = "Twitter" , value="<:twitterlogo:802493927735164969> [Click Here](https://twitter.com/warcrycodm)")
        em.set_image(url="https://cdn.discordapp.com/attachments/800083471082455080/800084854896590858/coollogo_com-949050.png")
        em.set_footer(text = "You dont need discord cause u r in it ;)" , icon_url = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn4.iconfinder.com%2Fdata%2Ficons%2Flogos-and-brands%2F512%2F91_Discord_logo_logos-512.png&imgrefurl=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F4373196%2Fdiscord_logo_logos_icon&tbnid=XhJRxzAZjY6zQM&vet=12ahUKEwiu2uSp9bHuAhVLGHIKHVdRAl4QMygAegUIARDDAQ..i&docid=FRt1msCuBLKlnM&w=512&h=512&q=discord%20logo%20png&ved=2ahUKEwiu2uSp9bHuAhVLGHIKHVdRAl4QMygAegUIARDDAQ")
        
        await ctx.send(embed = em)

    @commands.command(aliases = ["codes"])
    async def github(self , ctx):
        em = discord.Embed(title = "Bot's Github Repository" , description = "<:GitHubMark:805019234475704321> [Atidipt123/warcry](https://github.com/Atidipt123/warcry)" , color = discord.Color.green())
        await ctx.send(embed = em)

    @commands.command()
    async def about(self , ctx):
        em = discord.Embed(title = "About WarCry" , description = "WarCry gaming is a Call of Duty: Mobile clan based in Asia, who regularly compete for various tournaments, ranking events, and scrims with other clans. We are enthusiatic bunch of players who met through our passion for the game. Since inception, we have been able to form clan with members from various sections of society yet found comfort and competitiveness amongst each other to drive ourselves to become one of the top clans around the world." , color = discord.Color.dark_orange())
        em.add_field(name = "What we do?" , value = "We engage in chats daily, scrim together, and share every moment together, may it be of pure joy, maniacal laughter, or resentment over loosing a game. Together we are one, and would like you to join us in this journey filled with ups and downs. We are currently recruiting in Asia, and North America. So come join us, if you want a friendly digital space where you can play and have fun while achieving your personal gaming heights.")
        em.add_field(name="Why join us?" , value = "Friendly and chill clan members, you wont't imagine the amount of fun we have together regular scrims both internal and with other clans compete in almost every tournament that we can attend ")
        em.set_image(url="https://cdn.discordapp.com/attachments/802165222109610014/802165477618745383/a_1e54081c8b2c7de00a9c56d54e34096c_2.webp")
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Information(bot))