from discord.ext import commands
from dhooks import Webhook

import keys

from fg_discord.fg_messages import send_error

##### GLOBAL ERROR VALUES #####################################################
ERROR_ROLE = keys.error_role
ERROR_CHAN = keys.error_chan
ERROR_WEBHOOK = keys.error_webhook

ERROR_CODES = {
    'PLAYER001' : {'message' : 'Multiple matches on Discord Snowflake.'},
    'PLAYER002' : {'message' : 'Error in adding user to database.'},
}
###############################################################################

async def error_notify(ctx, command, code):
    """Sends error message to Officials."""
    message = f"<@&{ERROR_ROLE}> ERROR ON `{command}` by `{ctx.author.name}` ({ctx.author.id}) : `{code}` - "
    try:
        message += ERROR_CODES[code]['message']
    except:
        message += 'Unknown error.'
    
    await send_error(ctx, message)

async def send_user(ctx, message):
    """Sends discord private message to user."""
    await ctx.author.send(f"{ctx.author.mention} : {message}")

async def send_channel(ctx, message):
    """Sends discord message to channel."""
    await ctx.send(f"{ctx.author.mention} : {message}")


##### DISCORD FUNCTIONS #######################################################
class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
###############################################################################

async def setup(bot):
    await bot.add_cog(Errors(bot))