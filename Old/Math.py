from discord.ext import commands
from discord import app_commands

#This cog contains functions that allow the bot to do basic arithmetic
class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, arg1=None, *argv):
        flag = False
        try:
            sum = float(arg1)
        except:
            flag = True
            
        for arg in argv:
            if (flag):
                break
            try:
                sum = sum + float(arg)
            except ValueError:
                flag = True

        if (flag):
            await ctx.send(f'Invalid Input: Enter numbers seperated by spaces')
        else:        
            await ctx.send(f'= {sum}')


    ####################################################################################################################################



    @commands.command()
    async def mult(self, ctx, arg1=None, *argv):
        flag = False
        try:
            product = float(arg1)
        except:
            flag = True
        for arg in argv:
            if (flag):
                break
            try:
                product = product * float(arg)
            except ValueError:
                flag = True

        if (flag):
            await ctx.send(f'Invalid Input: Enter numbers seperated by spaces')
        else:        
            await ctx.send(f'= {product}')
            

    #################################################################################################################################


    @commands.command()
    async def sub(self, ctx, arg1=None, *argv):
        flag = False
        try:
            difference = float(arg1)
        except:
            flag = True

            
        for arg in argv:
            if (flag):
                break
            try:
                difference = difference - float(arg)
            except ValueError:
                flag = True
                
        if (flag):
            await ctx.send(f'Invalid Input: Enter numbers seperated by spaces')
        else:        
            await ctx.send(f'= {difference}')
            

    #######################################################################################################################


    @commands.command()
    async def div(self, ctx, arg1=None, *argv):
        flag = False

        try:
            quotient = float(arg1)
        except:
            flag = True
            
        for arg in argv:
            if (flag):
                break
            try:
                quotient = quotient / float(arg)
            except ValueError:
                flag = True
            except ZeroDivisionError:
                quotient = "Division by zero error"
                break

        if (flag):
            await ctx.send(f'Invalid Input: Enter numbers seperated by spaces')
        else:        
            await ctx.send(f'= {quotient}')        


async def setup(bot):
    await bot.add_cog(Math(bot))