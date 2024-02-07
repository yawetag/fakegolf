import asyncio
import colorama
import discord
import os
import requests

from discord.ext import commands
from discord.ext.commands import Bot
from fastapi import FastAPI

import keys

##### COLORAMA SETUP ##########################################################
colorama.init()
###############################################################################

##### DISCORD BOT SETUP #######################################################
TOKEN = keys.discord_token
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
bot = Bot(command_prefix="!", case_insensitive=True, intents=intents)
###############################################################################

##### FASTAPI SETUP ###########################################################
app = FastAPI()
###############################################################################

##### DISCORD FUNCTIONS #######################################################
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} running with FastAPI!")
    for filename in os.listdir('fg_discord'):
        if filename.endswith('.py'):
            print(f"Loading fg_discord.{filename[:-3]}")
            await bot.load_extension(f'fg_discord.{filename[:-3]}')
###############################################################################S

##### FASTAPI FUNCTIONS #######################################################
@app.get("/")
async def hello_world():
    return {"hello" : "world"}

@app.get("/players")
async def all_players():
    print("Got request for players.")
    return {'playerID' : 1, 'playerName' : 'yawetag'}
###############################################################################

##### INITIAL LOADING #########################################################
async def run():
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        await bot.logout()

asyncio.create_task(run())
###############################################################################