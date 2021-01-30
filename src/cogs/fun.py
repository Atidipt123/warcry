import discord
from discord.ext import commands
import random
import praw

reddit = praw.Reddit(client_id="ur client id",
                                client_secret="your client secret",
                                username="ur username",
                                password="ur password",
                                user_agent="praw")

class Fun(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command()
    async def meme(self , ctx):
        all_subs = []

        o = ["meme" , "dankmemes" , "memes"]

        for submission in reddit.subreddit(random.choice(o)).hot(limit=50):
            all_subs.append(submission)

        rm = random.choice(all_subs)

        name = rm.title
        url = rm.url

        em = discord.Embed(title=name , url = url)
        em.set_image(url=url)
        em.set_footer(text=f"👍 {rm.score} | 💬 {len(rm.comments)} | Posted by u/{rm.author}")

        await ctx.send(embed=em)

    @commands.command(aliases=["8ball"])
    async def _8ball(self , ctx , *, arg):
        res = ["As I see it, yes.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "It is certain.",
                "It is decidedly so."]

        await ctx.send(f"Question: {arg} \n Answer: {random.choice(res)}")

    @commands.command()
    async def coinflip(self , ctx):
        a = random.choice(["Heads" , "Tails"])
        await ctx.send(f"Its a {a}")

    @commands.command()
    async def noob(self , ctx , * , member: discord.Member = None):
        if member == None:
            member = ctx.author

        a = random.randrange(1 , 101)

        em = discord.Embed(title = f"Noob Percentage of {member.name}#{member.discriminator}" ,
                           description=f"{member.mention} is {a}% noob",
                           color=member.color)

        em.set_thumbnail(url =member.avatar_url)

        await ctx.send(embed=em)

    @commands.command()
    async def dog(self , ctx):
        all_subs = []


        for submission in reddit.subreddit("dogpictures").hot(limit=50):
            all_subs.append(submission)

        rm = random.choice(all_subs)

        name = rm.title
        url = rm.url

        em = discord.Embed(title=name , url = url)
        em.set_image(url=url)
        em.set_footer(text=f"👍 {rm.score} | 💬 {len(rm.comments)} | Posted by u/{rm.author}")

        await ctx.send(embed=em)

    @commands.command()
    async def cat(self , ctx):
        all_subs = []


        for submission in reddit.subreddit("catpictures").hot(limit=50):
            all_subs.append(submission)

        rm = random.choice(all_subs)

        name = rm.title
        url = rm.url

        em = discord.Embed(title=name , url = url)
        em.set_image(url=url)
        em.set_footer(text=f"👍 {rm.score} | 💬 {len(rm.comments)} | Posted by u/{rm.author}")

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Fun(bot))