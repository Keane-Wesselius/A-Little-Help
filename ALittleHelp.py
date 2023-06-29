import os
import discord
from discord.ext import commands


EXTENSIONS = [
    'cogs.Math', 
    'cogs.Secret_Message',
    'cogs.Misc',
    'cogs.Help',
    'cogs.Scraper',
    'cogs.GDrive',
    'cogs.Reminder']


TOKEN = open("/home/pi/Python/A-Little-Help/Token.txt", "r").readline()
GUILD = 'Davidamiright?'


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix = '!', intents = intents)






####################################################################################################################################################################

@bot.event
async def on_ready():
    #delete default help command
    bot.remove_command('help')

    for guild in bot.guilds:
        if guild.name == GUILD:
            break    

    for extension in EXTENSIONS:
        await bot.load_extension(extension)

    print(f'{bot.user} is connected to the following guild')
    print(f'Guild Name: {guild.name}')
    print(f'Guild ID: {guild.id}')
    

###########################################################################################################################################################################################

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "a little help" in message.content.lower():
        #await message.channel.send("Did you need my help?\nType !help to see how I can assist you")
        gif_file = discord.File("/home/pi/Python/A-Little-Help/ALittleHelp.gif", filename="ALittleHelp.gif")
        embed = discord.Embed(title="Did you need my help?", description="\nType !help to see what I can do!", colour = discord.Colour.green())
        embed.set_image(url="attachment://ALittleHelp.gif")
        await message.channel.send(file=gif_file, embed=embed)

    if str(message.author) == "Chicken-Chan#7185":
        await message.add_reaction("\N{Chicken}")
    
    userFilePath = "/home/pi/Python/A-Little-Help/Users/" + str(message.author.id) + ".txt"
    if not os.path.exists(userFilePath):
        file = open(userFilePath, "w")
        file.write("0")
        file.close()
    file = open(userFilePath, "r")
    numPosts = int(file.readline())
    file.close()
    numPosts += 1
    file = open(userFilePath, "w")
    file.write(str(numPosts))
    file.close()
    
    await bot.process_commands(message)





    

################################################################################################################################################################################

    #startReminder(ctx, timestamp, message)
    


    





bot.run(TOKEN)
