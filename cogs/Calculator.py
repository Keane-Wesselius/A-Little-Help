from discord.ext import commands
from discord import app_commands
import math
import re
import sys
sys.path.append('..')
import calculator.calculator as calc
#A cog is an extension to the discord bot 
#All cogs must follow the format shown here for it to work
#Each cog is a class with the methods of that class being the discord bot's features for that cog
class Calculator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="calculator", description="Calculator for +, -, *, /, ^")
    @app_commands.describe(expression="The math to calculate")
    async def calculate(self, interaction, expression:str):
        answer = calc.input_to_output(expression)
        await interaction.response.send_message(f"{expression} = {answer}")
        



async def setup(bot):
    await bot.add_cog(Calculator(bot))