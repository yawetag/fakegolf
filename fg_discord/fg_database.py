import pymysql

from discord.ext import commands

import keys

CONNECTION = pymysql.connect(
    host = keys.db_host,
    user = keys.db_user,
    password = keys.db_password,
    database = keys.db_database,
    autocommit = True,
    cursorclass = pymysql.cursors.DictCursor
)

##### DATABASE QUERIES ########################################################
def db_create(q, v):
    cur = CONNECTION.cursor()
    cur.execute(q, v)
    response = cur.lastrowid
    cur.close()

    return response

def db_read(q, v):
    cur = CONNECTION.cursor()
    cur.execute(q, v)
    response = cur.fetchall()
    cur.close()

    return response
###############################################################################

##### USER QUERIES ############################################################
def add_user_by_discord_id(ctx):
    player_name = ctx.author.name
    snowflake = ctx.author.id

    query = "INSERT INTO users (player_name, discord_snowflake) VALUES (%s, %s);"
    variables = (player_name, snowflake)
    response = db_create(query, variables)

    return response

def get_user_by_discord_id(snowflake):
    query = f"SELECT * FROM users WHERE discord_snowflake=%s;"
    variables = (snowflake)
    response = db_read(query, variables)
    
    return response
###############################################################################



##### DISCORD FUNCTIONS #######################################################
class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
###############################################################################

async def setup(bot):
    await bot.add_cog(Database(bot))