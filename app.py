import asyncio
import colorama
import discord

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
intents.message_content = True
activity = discord.Activity(type=discord.ActivityType.watching, name="Fake Golf")
bot = Bot(command_prefix="!", case_insensitive=True, intents=intents, activity=activity)
###############################################################################

##### FASTAPI SETUP ###########################################################
app = FastAPI()
###############################################################################

##### FASTAPI FUNCTIONS #######################################################
@app.get("/")
async def hello_world():
    return {"hello" : "world"}
###############################################################################

##### DISCORD FUNCTIONS #######################################################
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} running with FastAPI!")

@bot.command()
async def welcome(ctx: commands.Context, member: discord.Member):
    await ctx.send(f"Welcome to {ctx.guild.name}, {member.mention}!")

@bot.command()
async def yawetag(ctx):
    await ctx.send(f"YAWETAG!")
###############################################################################

##### INITIAL LOADING #########################################################
async def run():
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        await bot.logout()

asyncio.create_task(run())
###############################################################################