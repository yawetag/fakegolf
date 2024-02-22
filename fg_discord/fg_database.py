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
def db_read(q):
    cur = CONNECTION.cursor()
    cur.execute(q)
    response = cur.fetchall()
    cur.close()

    return response
###############################################################################

##### USER QUERIES ############################################################
def get_user_by_discord_id(snowflake):
    query = f"SELECT * FROM users WHERE discord_snowflake={snowflake};"
    response = db_read(query)
    
    return response
###############################################################################



##### DISCORD FUNCTIONS #######################################################
class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
###############################################################################

async def setup(bot):
    await bot.add_cog(Database(bot))