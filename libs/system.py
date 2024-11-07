from discord.ext import commands
class system(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @commands.command
    async def reload(self,ctx):
        await self.bot.load_extension("./libs/")#全てのpythonファイルを取得してforでルーぷするように
        await self.bot.load_extension("../modules/")#パスの確認をするように