from discord.ext import commands
from discord import app_commands


class Pokemon(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @app_commands.choices(time_unit=[
    app_commands.Choice(name='Bulbasaur', value=1),
    app_commands.Choice(name='Ivysaur', value=60),
    app_commands.Choice(name='Venusaur', value=1440),
    app_commands.Choice(name='Squirtle', value=1440),
    app_commands.Choice(name='Warturtle', value=1440),
    app_commands.Choice(name='Blastoise', value=1440),
    app_commands.Choice(name='Charmander', value=1440),
    app_commands.Choice(name='Charmelon', value=1440),
    app_commands.Choice(name='Charizard', value=1440),
    app_commands.Choice(name='Weedle', value=1440),
    app_commands.Choice(name='Kakuna', value=1440),
    app_commands.Choice(name='Beedril', value=1440),
    app_commands.Choice(name='Caterpie', value=1440),
    app_commands.Choice(name='Metapod', value=1440),
    app_commands.Choice(name='Butterfree', value=1440),
    app_commands.Choice(name='Paras', value=1440),
    app_commands.Choice(name='Parasect', value=1440),
    app_commands.Choice(name='Seel', value=1440),
    app_commands.Choice(name='Dugong', value=1440),
    app_commands.Choice(name='Wailmer', value=1440),
    app_commands.Choice(name='Wailord', value=1440),
    app_commands.Choice(name='Snorunt', value=1440),
    app_commands.Choice(name='Glalie', value=1440),
    app_commands.Choice(name='Sableye', value=1440),
    app_commands.Choice(name='Wingull', value=1440),
    app_commands.Choice(name='Pelliper', value=1440),
    app_commands.Choice(name='Ralts', value=1440),
    app_commands.Choice(name='Kirila', value=1440),
    app_commands.Choice(name='Guardivour', value=1440),
    app_commands.Choice(name='Wurmple', value=1440),
    app_commands.Choice(name='Cascoon', value=1440),
    app_commands.Choice(name='Silcoon', value=1440),
    app_commands.Choice(name='Dustox', value=1440),
    app_commands.Choice(name='Beautifly', value=1440),
    app_commands.Choice(name='Venusaur', value=1440)
    ])
    async def pokemon(self, interaction, poke:app_commands.Choice[int]):
        interaction.response.send_message(poke.name)

async def setup(bot):
    await bot.add_cog(Pokemon(bot))