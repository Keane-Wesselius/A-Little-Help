from discord.ext import commands

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    #@slash.slash(name="add", description="Add numbers")
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
    #@slash.slash(name="mult", description="Multiply numbers")
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
    #@slash.slash(name="sub", description="Subtract numbers")
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
    #@slash.slash(name="div", description="Divide numbers")
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