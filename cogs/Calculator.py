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

        expression = expression.replace("^", "**")
        

        try:
            await interaction.response.send_message(eval(expression))

        except SyntaxError:
            await interaction.response.send_message("ERROR: Syntax")

        #log stuff
        except ValueError:
            await interaction.response.send_message("ERROR: log can only accept numbers greater than 0")

        #for sets
        except TypeError:
            await interaction.response.send_message("ERROR: { } produces an error, try using ( ) instead")

        except ZeroDivisionError:
            await interaction.response.send_message("ERROR: divide by zero")

        except Exception:
            await interaction.response.send_message("Unknown Error")


async def setup(bot):
    await bot.add_cog(Calculator(bot))