import discord
from .libs import config
intents = discord.Intents.default()
intents.all = True
client = discord.Client(intents=intents)
client.run("token_tmp")
def run():
    config.config().load()