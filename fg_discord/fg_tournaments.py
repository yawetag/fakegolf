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
    
    def t_get_tournaments(self):
        tournaments = db.get_all_tournaments()  # Get list of tournaments
        if tournaments is None:
            return 0
        else:
            return tournaments
    
    def t_tournament_info(self, tid):
        """Gets information about a tournament."""
        tournaments = db.get_tournament_info(tid)
        if tournaments is None:
            return 0
        else:
            return tournaments
    
    @commands.command(
            brief="See list of tournaments.",
            description="-tournaments\nSee list of tournaments in Fake Golf.",
            aliases=['t_list']
    )
    async def tournaments(self, ctx):
        tournaments = Tournaments.t_get_tournaments(self)
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

    @commands.command(
        brief="See detail of tournament.",
        description="-tournament_info <number>\nSee details of tournament by number.",
        aliases=['t_info']
    )
    async def tournament_info(self, ctx, tournament_id=0):
        tournament = Tournaments.t_tournament_info(self, tournament_id)
        if tournament == 0:
            await error_notify(ctx, "tournaments.tournament_info", "TOURNAMENTS001")
            message = "There has been an error in your command. Admins will look into it and contact you."
        elif len(tournament) == 0:
            message = "There are no tournaments matching that id. Please type `-tournaments` to see all active tournaments."
        else:
            message = f"Here is information on **{tournament[0]['tournament_name']}** by {tournament[0]['player_name']}:\n"
            for t in tournament:
                message += f"   Round {t['round']}: **{t['course_name']}** (par: {t['par']}. yards: {t['yardage']:,})\n"
            message += f"To join the tournament, type `-join_tournament {tournament_id}`"
        await send_channel(ctx, message)
###############################################################################

async def setup(bot):
    await bot.add_cog(Tournaments(bot))