import discord
import requests

from discord.ext import commands

##### DISCORD FUNCTIONS #######################################################
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}.")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}~")
        else:
            await ctx.send(f"Hello {member.name}... This feels familiar.")
        self._last_member = member

    @commands.command()
    async def yawetag(self, ctx):
        await ctx.send(f"YAWETAG!")

    @commands.command()
    async def players(self, ctx):
        print("Sending request for players")
        response = requests.get('http://127.0.0.1:8000/players')
        await ctx.send("Got response!")

###############################################################################

async def setup(bot):
    await bot.add_cog(Test(bot))