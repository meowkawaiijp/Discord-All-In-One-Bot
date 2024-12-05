from discord.ext import commands
class system(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command
    async def reload(self,ctx):
        for pyf,pyf2 in zip(files_1,files_2):
         await self.bot.load_extension(f"./libs/{pyf}")#全てのpythonファイルを取得してforでルーぷするように
         await self.bot.load_extension(f"../modules/{pyf2}")#パスの確認をするように