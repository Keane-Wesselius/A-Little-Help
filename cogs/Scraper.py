from discord.ext import commands
from ..webscraper import webScraper as scraper

class Scraper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx, *args):
        if (args):
            args = " ".join(args)
            url = scraper.getYoutubeVideo(args)
            if url:
                await ctx.send(url)
            else:
                await ctx.send("Oops I could'nt find a video for you...")
        else:
            url = scraper.getYoutubeVideo("muntjac")
            if url:
                await ctx.send(url)
            else:
                await ctx.send("Oops I could'nt find a video for you...")

async def setup(bot):
    await bot.add_cog(Scraper(bot))