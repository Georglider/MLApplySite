from mlapplysite.blueprints.oauth2.login import login
import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('test')

def start():
    client.run("OTEyMDYzNTMzMDgzMTYwNjA3.YZqfWw.FI9Fyqgpna26C569fHXgiAl_cUA")