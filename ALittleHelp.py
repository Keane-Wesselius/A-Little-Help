import os
import discord
from discord.ext import commands

#List to hold all the cogs (bot commands in other files)
EXTENSIONS = [
    'cogs.Math',
    'cogs.Gamble',
    'cogs.Secret_Message',
    'cogs.Misc',
    'cogs.Help',
    'cogs.Scraper',
    'cogs.GDrive',
    'cogs.Reminder']


#Discord token must be kept secret
TOKEN = open("/home/pi/Python/A-Little-Help/Token.txt", "r").readline()
#A guild name to make sure the bot has connected
GUILD = 'Davidamiright?'


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix = '!', intents = intents)







####################################################################################################################################################################

#called when the bot is ready
@bot.event
async def on_ready():
    #delete default help command so we can implement our own
    bot.remove_command('help')


    for guild in bot.guilds:
        if guild.name == GUILD:
            break    

    #loads the cogs, just the other bot commands in other files
    for extension in EXTENSIONS:
        await bot.load_extension(extension)

    #updates slash commands
    await bot.tree.sync()

    #This print statement is for the developer to know when the bot is ready to be used
    print(f'{bot.user} is connected to the following guild')
    print(f'Guild Name: {guild.name}')
    print(f'Guild ID: {guild.id}')
    

###########################################################################################################################################################################################

@bot.event
async def on_message(message):
    #make sure the bot does not respond to itself
    if message.author == bot.user:
        return
    #checks if "a little help" is in the message and will message if it is
    if "a little help" in message.content.lower():
        #await message.channel.send("Did you need my help?\nType !help to see how I can assist you")
        gif_file = discord.File("/home/pi/Python/A-Little-Help/ALittleHelp.gif", filename="ALittleHelp.gif")
        embed = discord.Embed(title="Did you need my help?", description="\nType !help to see what I can do!", colour = discord.Colour.green())
        embed.set_image(url="attachment://ALittleHelp.gif")
        await message.channel.send(file=gif_file, embed=embed)

    #How to add a reaction to a message
    if str(message.author) == "Chicken-Chan#7185":
        await message.add_reaction("\N{Chicken}")
    

    userFilePath = "/home/pi/Python/A-Little-Help/users/" + str(message.author.id) + ".txt"
    try:
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
    except Exception:
        pass
        #this try except block counts the number of times a user posts to a server with the bot in it
        #occasionally the file will not be opened and error out. It is not important to accurately count
        #every single post so we just pass on the exception

    
    await bot.process_commands(message)








#Starts the bot
if __name__ == '__main__':
    while True:
        try:
            bot.run(TOKEN)
        except ConnectionClosed:
            pass




#Notes
#SLASH COMMAND NAMES MUST BE ALL LOWERCASE
#SLASH ARGUMENTS MUST ALSO BE ALL LOWERCASE
#SLASH COMMANDS WILL NOT SYNC AND UPDATE IF THERE IS AN ERROR WITH A SLASH COMMAND
