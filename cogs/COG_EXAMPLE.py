from discord.ext import commands
from discord import app_commands

#A cog is an extension to the discord bot 
#All cogs must follow the format shown here for it to work
#Each cog is a class with the methods of that class being the discord bot's features for that cog
class COG_NAME(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


#This function must be provided to add the cog to the discord bot
#COG_NAME must be the same name as the class above
#This function is called by the discord bot so all you need to do is define it in a cog file
async def setup(bot):
    await bot.add_cog(COG_NAME(bot))