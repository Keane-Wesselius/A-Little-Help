from discord.ext import commands
from discord import app_commands
import random

#A cog is an extension to the discord bot 
#All cogs must follow the format shown here for it to work
#Each cog is a class with the methods of that class being the discord bot's features for that cog
class Gamble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="coin", description="Flip a coin, Heads or Tails")
    async def flip(self, interaction):
        chance = random.randint(0, 1)
        coin = "Heads"
        if chance == 0:
            coin = "Tails"
        await interaction.response.send_message(coin)

    @app_commands.command(name="dice", description="Rolls a dice")
    @app_commands.describe(sides="How many sides are on the dice")
    async def dice(self, interaction, sides:app_commands.Range[int, 1] = 6):
        roll = random.randint(1, sides)
        await interaction.response.send_message(roll)
    





#This function must be provided to add the cog to the discord bot
#COG_NAME must be the same name as the class above
#This function is called by the discord bot so all you need to do is define it in a cog file
async def setup(bot):
    await bot.add_cog(Gamble(bot))