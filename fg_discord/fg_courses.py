import asyncio
import discord
import requests

from discord.ext import commands

import fg_discord.fg_database as db
from fg_discord.fg_messages import send_user, send_channel
from fg_discord.fg_errors import error_notify

##### DISCORD FUNCTIONS #######################################################
class Courses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_courses(self):
        courses = db.get_all_courses()  # Get list of courses
        if courses is None:
            return 0
        else:
            return courses
    
    @commands.command(
            brief="See list of courses.",
            description="-courses\nSee list of courses in Fake Golf."
    )
    async def courses(self, ctx):
        courses = Courses.get_courses(self)
        if courses == 0:
            await error_notify(ctx, "courses.courses", "COURSES001")
            message = "There has been an error in your command. Admins will look into it and contact you."
        else:
            message = f"Here is a list of courses:\n"
            for c in courses:
                message += f"1. {c['course_name']} by {c['player_name']}. Par {c['par']}. {c['yardage']:,} yards.\n"

        await send_channel(ctx, message)

###############################################################################

async def setup(bot):
    await bot.add_cog(Courses(bot))