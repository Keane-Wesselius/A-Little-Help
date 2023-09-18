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
        url = self.google.createDoc(interaction.guild, file_name)
        await interaction.response.send_message(url)

    #Creates a google slide file and shares the link, if no filename is given a default one is picked
    @commands.command()
    async def createSlide(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.createSlide(ctx.guild.name, args)
            await ctx.send(url)
        else:
            url = self.google.createSlide(ctx.guild.name)
            await ctx.send(url)

    #Creates a google sheet file and shares the link, if no filename is given a default one is picked
    @commands.command()
    async def createSheet(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.createSheet(ctx.guild.name, args)
            await ctx.send(url)
        else:
            url = self.google.createSheet(ctx.guild.name)
            await ctx.send(url)

    @commands.command()
    async def getFile(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.getDoc(ctx.guild.name, args)
            await ctx.send(url)
        else:
            await ctx.send("You need to specify a filename to get")





async def setup(bot):
    await bot.add_cog(GDrive(bot))