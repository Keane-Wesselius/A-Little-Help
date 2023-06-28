from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.BOT_LINK = open("/home/pi/Python/A-Little-Help/botAccessLink.txt", "r").readline()

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' Pong! {round(self.bot.latency * 1000)}ms')


    @commands.command()
    #@commands.is_owner()
    async def info(self, ctx):
        await ctx.send(f'Bot Info = {self.bot.user} \nUser ID = {ctx.author}\nGuild Name = {ctx.guild} \nGuild ID = {ctx.guild.id}\nUse !help for help with commands')

    @commands.command()
    #@slash.slash(name="addBot", description="Creates link to this add bot to a server")
    async def addBot(self, ctx):
        await ctx.send(self.BOT_LINK)

async def setup(bot):
    await bot.add_cog(Misc(bot))