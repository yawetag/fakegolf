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

def db_read(q, v=None):
    cur = CONNECTION.cursor()
    if v is not None:
        cur.execute(q, v)
    else:
        cur.execute(q)
    response = cur.fetchall()
    cur.close()

    return response

def db_update(q, v):
    cur = CONNECTION.cursor()
    cur.execute(q, v)
    response = cur.rowcount
    cur.close()

    return response
###############################################################################

##### COURSES QUERIES #########################################################
##### Read ####################################################################
def get_all_courses():
    query = "SELECT c.id, c.course_name, u.player_name, c.par, c.yardage FROM courses c LEFT JOIN users u ON c.designer_id = u.id;"
    response = db_read(query)
    
    return response
###############################################################################
###############################################################################

##### TOURNAMENTS QUERIES #####################################################
##### Read ####################################################################
def get_all_tournaments():
    query = "SELECT t.id, t.tournament_name, u.player_name, COUNT(*) AS 'rounds' FROM tournaments t LEFT JOIN users u ON t.designer_id = u.id LEFT JOIN tournament_rounds tr ON tr.tournament_id=t.id;"
    response = db_read(query)
    
    return response
###############################################################################
###############################################################################

##### USER QUERIES ############################################################
##### Create ##################################################################
def add_user_by_discord_id(ctx):
    """Adds new user to users table with their discord snowflake."""
    player_name = ctx.author.name
    snowflake = ctx.author.id

    query = "INSERT INTO users (player_name, discord_snowflake) VALUES (%s, %s);"
    variables = (player_name, snowflake)
    response = db_create(query, variables)

    return response
###############################################################################

##### Read ####################################################################
def get_user_by_discord_id(snowflake):
    """Gets user information with their discord snowflake."""
    query = "SELECT * FROM users WHERE discord_snowflake=%s;"
    variables = (snowflake)
    response = db_read(query, variables)
    
    return response
###############################################################################

##### Update ##################################################################
def change_name_by_discord_id(ctx, new_name):
    """Changes player_name in users table by their discord snowflake."""
    snowflake = ctx.author.id
    query = "UPDATE users set player_name=%s WHERE discord_snowflake=%s;"
    variables = (new_name, snowflake)
    response = db_update(query, variables)

    return response
###############################################################################

##### Delete ##################################################################
###############################################################################
###############################################################################



##### DISCORD FUNCTIONS #######################################################
class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
###############################################################################

async def setup(bot):
    await bot.add_cog(Database(bot))