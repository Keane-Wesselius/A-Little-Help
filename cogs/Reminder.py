from discord.ext import commands
import threading
import asyncio
import time
from datetime import datetime

class Reminder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.date_format = '%m-%d-%Y %H:%M:%S'
        #example = '06-25-2023 13:00:00'

    def timer(self, ctx, timeup, message):
        while True:
            if time.time() >= timeup:
                asyncio.run_coroutine_threadsafe(ctx.send("@everyone " + message), self.bot.loop)
                return

    def timerAsyncWrapper(self, ctx, timeup, message):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        future = asyncio.ensure_future(self.timer(ctx, timeup, message)) # tasks to do
        loop.run_until_complete(future)

        #asyncio.get_event_loop().create_task(timer(ctx, timeup, message))

    def startReminder(ctx, timestamp, timer_message):

        t = threading.Thread(target=self.timerAsyncWrapper, args=(ctx, timestamp, timer_message,))
        t.start()


    def convertToTimestamp(self, date_string):
        #Turn date and time string into a datetime object
        date_time = datetime.strptime(date_string, self.date_format)
        # Convert the datetime object to a timestamp
        timestamp = datetime.timestamp(date_time)
        return timestamp

    @commands.command()
    async def reminder(self, ctx, date=None, time=None, *args):
        message = "Reminder"
        if date == None:
            await ctx.send("Date not specified")
            return
        if time == None:
            await ctx.send("Time not specified")
            return
        if (args):
            message = " ".join(args)
        

            
        date_string = date + " " + time
        try:
            timestamp = self.convertToTimestamp(date_string)
        except Exception as e:
            await ctx.send("Invalid date or time must be in the form M-D-Y H:M:S" + " " + str(e))
            return
        
        thread = threading.Thread(target=self.timer, args=(ctx, timestamp, message,))
        thread.start()
        await ctx.send("Reminder Created!")






async def setup(bot):
    await bot.add_cog(Reminder(bot))
