from discord.ext import commands

class Secret_Message(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.CODE_KEY = 250
        self.SECRET_ERROR = "Spaghetti"


    

    @commands.command()
    #@slash.slash(name="encode", description="Scambles text")
    async def encode(self, ctx, *args):
        message = ""
        if (args):
            args = " ".join(args)
            for element in args:
                element = chr(ord(element) + self.CODE_KEY)
                message += element
            await ctx.send(message)
        else:
            for element in self.SECRET_ERROR:
                element = chr(ord(element) + self.CODE_KEY)
                message += element
            await ctx.send(message)


    ###############################################################################################################################



    @commands.command()
    #@slash.slash(name="decode", description="Descrambles text")
    async def decode(self, ctx, *args):
        message = ""
        if (args):
            args = " ".join(args)
            for element in args:
                element = chr(ord(element) - self.CODE_KEY)
                message += element
            await ctx.send(message)
        else:
            await ctx.send("Invalid Input: You must provide text to decode")


async def setup(bot):
    await bot.add_cog(Secret_Message(bot))