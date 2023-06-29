from discord.ext import commands
import sys
sys.path.append('..')
import google.doc_creator



class GDrive(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.google = doc_creator.Doc_Creator()


    @commands.command()
    #@slash.slash(name="createDoc", description="Creates a Google Doc file")
    async def createDoc(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.createDoc(args)
            await ctx.send(url)
        else:
            url = self.google.createDoc()
            await ctx.send(url)


    @commands.command()
    #@slash.slash(name="createSlide", description="Creates a Google Slide file")
    async def createSlide(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.createSlide(args)
            await ctx.send(url)
        else:
            url = self.google.createSlide()
            await ctx.send(url)


    @commands.command()
    #@slash.slash(name="createSheet", description="Creates a Google Sheet file")
    async def createSheet(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = self.google.createSheet(args)
            await ctx.send(url)
        else:
            url = self.google.createSheet()
            await ctx.send(url)





async def setup(bot):
    await bot.add_cog(GDrive(bot))