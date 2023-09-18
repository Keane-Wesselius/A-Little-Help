from discord.ext import commands
from discord import app_commands
import sys
sys.path.append('..')
import webscraper.webScraper as scraper

class Scraper(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="youtube", description="Finds a Youtube video based on your search query")
    @app_commands.describe(search="Youtube video to search for")
    @app_commands.rename(search="Query")
    async def youtube(self, interaction, search: str):
        url = scraper.getYoutubeVideo(search)
        if url:
            await interaction.response.send_message(url)
        else:
            await interaction.response.send_message("Oops I could'nt find a video for you...")


async def setup(bot):
    await bot.add_cog(Scraper(bot))