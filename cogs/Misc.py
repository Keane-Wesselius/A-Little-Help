from discord.ext import commands
from discord import app_commands

#Cog for the miscelanous commands for the bot that dont really have their own place
class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.BOT_LINK = open("/home/pi/Python/A-Little-Help/botAccessLink.txt", "r").readline()

    #Get the ping of the bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' Pong! {round(self.bot.latency * 1000)}ms')

    #Prints some info about the bot, the user who asked, and the guild
    @commands.command()
    #@commands.is_owner()
    async def info(self, ctx):
        await ctx.send(f'Bot Info = {self.bot.user} \nUser ID = {ctx.author}\nGuild Name = {ctx.guild} \nGuild ID = {ctx.guild.id}\nUse !help for help with commands')

    #Provides a link that allows you to add the bot to another server
    @commands.command()
    async def addBot(self, ctx):
        await ctx.send(self.BOT_LINK)

    @app_commands.command(name="test", description="I hope this works")
    @app_commands.describe(word="The word you want me to say")
    @app_commands.rename(member='whatever_you_want')
    async def test(self, interaction, word):
        await interaction.response.send_message(f'you typed {word}')


async def setup(bot):
    await bot.add_cog(Misc(bot))