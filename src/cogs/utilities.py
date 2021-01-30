import discord
from discord.ext import commands

class Utilities(commands.Cog):
    def __init__(self , bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self ,ctx, *, msg):
        await ctx.message.delete()
        if msg != None:
            for member in ctx.guild.members:
                try:
                    if member.dm_channel != None:
                        await member.dm_channel.send(msg)
                    else:
                        await member.create_dm()
                        await member.dm_channel.send(msg)
                except:
                    continue

    @commands.command()
    async def afk(self , ctx):
        user = ctx.author
        await user.edit(nick=f"[AFK]{user.display_name}")
        await ctx.send("Marked ur nickname as [AFK]. If u want to remove afk just type `$removeafk`")

    @commands.command()
    async def removeafk(self , ctx):
        user = ctx.author
        if user.display_name.startswith("[AFK]"):
            await user.edit(nick=user.name)
            await ctx.send("Done to change ur nickname use `$selfnick [nickname]`")
        else:
            await ctx.send("You r not marked as afk!")

    @commands.command()
    async def selfnick(self , ctx , * , nickname):
        await ctx.author.edit(nick=nickname)
        await ctx.send(f"Changed ur nickname to `{nickname}`")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self , ctx , user: discord.Member = None , * , reason = None):
        if reason == None:
            reason = "Not specified."

        if user == ctx.author or user == None:
            await ctx.send(":negative_squared_cross_mark: Are u planning to ban urself?")

        else:
            await user.ban(reason=reason)
            await ctx.send(f"Banned __**{user.name}#{user.discriminator}**__.\nReason - **{reason}**\nResponsible Moderator - {ctx.author.mention}")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self , ctx , user: discord.Member):
        if reason == None:
            reason = "Not specified."

        if user == ctx.author or user == None:
            await ctx.send(":negative_squared_cross_mark: Are u planning to kick urself?")

        else:
            await user.kick(reason=reason)
            await ctx.send(f"Kicked __**{user.name}#{user.discriminator}**__.\nReason - **{reason}**\nResponsible Moderator - {ctx.author.mention}")

    @commands.command(aliases=["nick"])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self , ctx , user: discord.Member , * , nick):
        await user.edit(nick=nick)
        await ctx.send(f"Changed Nickname for `{user.name}#{user.discriminator}` `{nick}`")

def setup(bot):
    bot.add_cog(Utilities(bot))