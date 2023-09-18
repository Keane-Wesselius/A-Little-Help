from discord.ext import commands
from discord import app_commands

#Cog for the miscelanous commands for the bot that dont really have their own place
class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.BOT_LINK = open("/home/pi/Python/A-Little-Help/botAccessLink.txt", "r").readline()

    #Get the ping of the bot
    #SLASH COMMAND NAMES MUST BE ALL LOWERCASE
    @app_commands.command(name='ping', description="Get bot's latenecy")
    async def ping(self, interaction):
        await interaction.response.send_message(f' Pong! {round(self.bot.latency * 1000)}ms')

    #Prints some info about the bot, the user who asked, and the guild
    @commands.command()
    async def info(self, ctx):
        await ctx.send(f'Bot Info = {self.bot.user} \nUser ID = {ctx.author}\nGuild Name = {ctx.guild} \nGuild ID = {ctx.guild.id}\nUse !help for help with commands')

    #Provides a link that allows you to add the bot to another server
    @commands.command()
    @commands.is_owner()
    async def addBot(self, ctx):
        await ctx.send(self.BOT_LINK)


    @app_commands.command(name="test", description="I hope this works")
    @app_commands.choices(day=[
    app_commands.Choice(name='Monday', value=1),
    app_commands.Choice(name='Tuesday', value=2)
])
    async def test(self, interaction, day: app_commands.Choice[int]):
        await interaction.response.send_message(day.name)


async def setup(bot):
    await bot.add_cog(Misc(bot))