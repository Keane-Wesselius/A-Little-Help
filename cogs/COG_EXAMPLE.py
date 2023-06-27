from discord.ext import commands

class COG_NAME(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


async def setup(bot):
    await bot.add_cog(COG_NAME(bot))