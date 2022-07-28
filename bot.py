from discord.ext import commands
from loguru import logger
import discord
import sqlite3
import traceback
from discord.utils import get
import discord

data = sqlite3.connect('server.db', check_same_thread=False)
sql = data.cursor()



intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="?", intents=intents)

@client.event
async def on_ready():
    logger.debug(f"Conncted!")


@client.event
async def on_member_join(member):
    print(member)
    guild = member.guild
    name = member.name
    if member.id == int(data.execute(f"SELECT user_id FROM users").fetchone()[0]):
        role = discord.utils.get(member.guild.roles, name="ML")
        await member.add_roles(role)

@client.command()
async def test(ctx):
    for i in ctx.guild.roles:
        print(i.name)


# Запускает клиент       
client.run("OTI2ODk3OTcwMTIzNzg4Mjk5.YdCXAQ.btb5ybE4YLR97WZ24V3hwmoZpso")
