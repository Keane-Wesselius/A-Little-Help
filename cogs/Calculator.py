from discord.ext import commands
from discord import app_commands
import math
import re

#A cog is an extension to the discord bot 
#All cogs must follow the format shown here for it to work
#Each cog is a class with the methods of that class being the discord bot's features for that cog
class Calculator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def cos(self, x): 
        return math.cos(x)
    def sin(self, x): 
        return math.sin(x)
    def tan(self, x): 
        return math.tan(x)
    def cot(self, x):
        return math.cos(x)/ math.sin(x)
    def log(self, x):
        return math.log(x, 10)
    def ln(self, x):
        return math.log(x)

    @app_commands.command(name="calc", description="Calculator")
    @app_commands.describe(expression="The math to calculate")
    async def calc(self, interaction, expression:str):
        pass


    def shunting_yard(self, orginal_equation:str):
        equation = orginal_equation
        shunted = []
        while len(equation > 0):
            current = equation[0]

            if current.isdigit():
                if len(equation > 1):
                    i = 1
                    if (equation[i].isdigit() or equation[i] == '.'):                  
                        while True:
                            if len(equation) > i + 1 and (equation[i + 1].isdigit() or equation[i + 1] == '.'):
                                i += 1
                            else:
                                break
                        current = equation[0:i]
                        shunted.append(current)
                        if len(equation) > i+1:
                            equation = equation[i+1:]
                        continue
                    equation = equation[1:]

                shunted.append(current)

            else:
                if len(equation) > 1:
                    equation = equation[1:]
                



async def setup(bot):
    await bot.add_cog(Calculator(bot))