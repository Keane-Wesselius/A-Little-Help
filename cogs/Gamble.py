from discord.ext import commands
from discord import app_commands
import random


class Gamble(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="flip_coin", description="Flips a coin, Heads or Tails")
    async def flip(self, interaction):
        chance = random.randint(0, 1)
        coin = "Heads"
        if chance == 0:
            coin = "Tails"
        await interaction.response.send_message(coin)

    @app_commands.command(name="roll_dice", description="Rolls a dice, defaults to 6 sides if not specified")
    @app_commands.describe(sides="How many sides are on the dice")
    async def dice(self, interaction, sides:app_commands.Range[int, 1] = 6):
        roll = random.randint(1, sides)
        await interaction.response.send_message(roll)
    



async def setup(bot):
    await bot.add_cog(Gamble(bot))