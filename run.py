import discord
from discord.ext import commands
from .libs import config,system
from .modules import backup_module,test_module
intents = discord.Intents.default()
intents.all = True
client = commands.Bot(command_prefix='>>', intents=intents)
configs = None
def run():
    configs = config.config().load()
    client.add_cog(system.system(client))
    client.add_cog(backup_module.backup(client))
@client.evenet
async def on_ready():
    print("[*] successfully!!")
    print(f"Servers: {len(client.fetch_guilds)} Memebers: {len(client.get_all_members)}")
run()
client.run(configs['token'])