import discord
from discord.ext import commands
class backup(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command()
    async def backup(self,ctx,save_file_path="./config/saves/server/"):
        #for ctx.guilds
         await ctx.send(f"Hello World! {save_file_path}")