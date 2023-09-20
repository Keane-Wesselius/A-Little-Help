from discord.ext import commands
from discord import app_commands

class Secret_Message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.CODE_KEY = 250
        self.SECRET_ERROR = "Spaghetti"


    

    @app_commands.command(name="encode", description="Scrambles text")
    @app_commands.describe(secret_message="The text you want scrambled")
    async def encode(self, interaction, secret_message:str):
        message = ""
        for element in secret_message:
            element = chr(ord(element) + self.CODE_KEY)
            message += element
        await interaction.response.send_message(message)


    ###############################################################################################################################



    @app_commands.command(name="decode", description="Unscrambles text from encode")
    @app_commands.describe(secret_message="The text you want unscrambled")
    async def decode(self, interaction, secret_message:str):
        message = ""
        for element in secret_message:
            element = chr(ord(element) + self.CODE_KEY)
            message += element
        await interaction.response.send_message(message)


async def setup(bot):
    await bot.add_cog(Secret_Message(bot))