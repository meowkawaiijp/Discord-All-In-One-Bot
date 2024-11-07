import discord
from discord.ext import commands
from .libs import config,system
from .modules import backup_module,test_module
intents = discord.Intents.default()
intents.all = True
client = commands.Bot(command_prefix='>>', intents=intents)
configs = None
def run():
    cinfigs = config.config().load()
    client.add_cog(system.system(client))
    client.add_cog(backup_module.backup(client))
run()
client.run(configs['token'])