import asyncio
import discord
import requests

from discord.ext import commands

import fg_discord.fg_database as db
from fg_discord.fg_messages import send_user, send_channel
from fg_discord.fg_errors import error_notify

##### DISCORD FUNCTIONS #######################################################
class Tournaments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_tournaments(self):
        tournaments = db.get_all_tournaments()  # Get list of tournaments
        if tournaments is None:
            return 0
        else:
            return tournaments
    
    @commands.command(
            brief="See list of tournaments.",
            description="-tournaments\nSee list of tournaments in Fake Golf."
    )
    async def tournaments(self, ctx):
        tournaments = Tournaments.get_tournaments(self)
        if tournaments == 0:
            await error_notify(ctx, "tournaments.tournaments", "TOURNAMENTS001")
            message = "There has been an error in your command. Admins will look into it and contact you."
        else:
            message = f"Here is a list of tournaments:\n"
            for t in tournaments:
                message += f"   (#{t['id']}) **{t['tournament_name']}** by {t['player_name']}. {t['rounds']} {'round' if t['rounds']==1 else 'rounds'}.\n"
        message += "\nFor more information on a tournament, type `-tournament_info <#>`, where `<#>` is the tournament number."
        message += "\nTo join a tournament, type `-join_tournament <#>` where `<#>` is the tournament number."

        await send_channel(ctx, message)

###############################################################################

async def setup(bot):
    await bot.add_cog(Tournaments(bot))