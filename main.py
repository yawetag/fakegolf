import asyncio
import discord
import os
import requests

from discord.ext import commands
from discord.ext.commands import Bot
from fastapi import FastAPI

import keys

##### DISCORD BOT SETUP #######################################################
TOKEN = keys.discord_token
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.playing, name="Fake Golf")
bot = Bot(command_prefix="-", case_insensitive=True, intents=intents, activity=activity)
###############################################################################

##### DISCORD FUNCTIONS #######################################################
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} in the following servers:")
    for guild in bot.guilds:
        print(f"   {guild.name} (id: {guild.id})")
    print()
    print(f"Loading the following modules:")
    for filename in os.listdir('fg_discord'):
        if filename.endswith('.py'):
            print(f"   fg_discord.{filename[:-3]}")
            await bot.load_extension(f'fg_discord.{filename[:-3]}')
bot.run(TOKEN)
###############################################################################S