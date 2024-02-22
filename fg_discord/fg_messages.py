from dhooks import Webhook
from discord.ext import commands

import keys

async def send_channel(ctx, message):
    """Sends discord message to channel."""
    await ctx.send(f"{ctx.author.mention} : {message}")

async def send_error(ctx, message):
    """Sends error message to error channel."""
    hook = Webhook(keys.error_webhook)
    hook.send(message)


async def send_user(ctx, message):
    """Sends discord private message to user."""
    await ctx.author.send(f"{ctx.author.mention} : {message}")



##### DISCORD FUNCTIONS #######################################################
class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
###############################################################################

async def setup(bot):
    await bot.add_cog(Messages(bot))