from discord.ext import commands
from discord import app_commands
import sys
sys.path.append('..')
import google.doc_creator as doc_creator


#This cog provides the bot with functionality to create Google docs, sheets, and slides.
#The resulting file is shared via a link that allows anyone with the link to edit the files
#Used to help speed up coloborations with others so no waiting for file creation and changing of permissions
class GDrive(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.google = doc_creator.Doc_Creator()

    #Creates a google doc file and shares the link, if no filename is given a default one is picked
    @app_commands.command(name="create_doc", description="Creates a new Google Doc and returns a link")
    @app_commands.describe(file_name="The name of the file you are creating")
    async def create_doc(self, interaction, file_name:str):
        await interaction.response.send_message("Please wait while I create that Doc for you")
        await self.google.createDoc(interaction, file_name)

    #Creates a google slide file and shares the link, if no filename is given a default one is picked
    @app_commands.command(name="create_slide", description="Creates a new Google Slide and returns a link")
    @app_commands.describe(file_name="The name of the file you are creating")
    async def create_slide(self, interaction, file_name:str):
        await interaction.response.send_message("Please wait while I create that Slide for you")
        await self.google.createSlide(interaction, file_name)

    #Creates a google sheet file and shares the link, if no filename is given a default one is picked
    @app_commands.command(name="create_sheet", description="Creates a new Google Sheet and returns a link")
    @app_commands.describe(file_name="The name of the file you are creating")
    async def create_sheet(self, interaction, file_name:str):
        await interaction.response.send_message("Please wait while I create that Sheet for you")
        await self.google.createSheet(interaction, file_name)


    @app_commands.command(name="get_file", description="Returns a link to a previously created Google document")
    @app_commands.describe(file_name="The name of the file you are looking for")
    async def get_file(self, interaction, file_name:str):
        await interaction.response.send_message("Please wait while I find that file for you")
        await self.google.getDoc(interaction, file_name)






async def setup(bot):
    await bot.add_cog(GDrive(bot))