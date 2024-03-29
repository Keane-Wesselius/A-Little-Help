from discord.ext import commands
import threading
import asyncio
import time
import re
from datetime import datetime

class Reminder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.date_format = '%m-%d-%Y %H:%M:%S'
        self.re_date = r'\d{2}-\d{2}-\d{4}'
        self.re_time = r'\d{2}:\d{2}:\d{2}'
        self.re_num =  r'^\d+$'
        self.re_alpha =  r'^[a-zA-Z]+$'
        #example = '06-25-2023 13:00:00'

    #Thread Function
    def timer(self, interaction, timeup, message):
        while True:
            if time.time() >= timeup:
                asyncio.run_coroutine_threadsafe(interaction.followup.send("@everyone " + message), self.bot.loop)
                return


    def convertToTimestamp(self, date_string):
        #Turn date and time string into a datetime object
        date_time = datetime.strptime(date_string, self.date_format)
        # Convert the datetime object to a timestamp
        timestamp = datetime.timestamp(date_time)
        return timestamp
    
    def convertInputToDateString(self, date, time):
        if re.match(self.re_date, date) and re.match(self.re_time, time):
            date_string = date + " " + time
            return date_string
        elif re.match(self.re_time, date):
            current_date = datetime.now()
            current_date = current_date.strftime('%m-%d-%Y')
            date_string = current_date + " " + date
            return date_string
        elif re.match(self.re_date, date) and time == None:
            current_time = datetime.now()
            current_time = current_time.strftime('%H:%M:%S')
            date_string = date + " " + current_time
            return date_string

    @commands.command()
    async def reminder(self, ctx, date=None, time=None, *args):
        message = "Reminder"
        date_string = ""

        if args != None:
            message = " ".join(args)
        
        date_string = self.convertInputToDateString(date, time)

            
        try:
            timestamp = self.convertToTimestamp(date_string)
        except Exception as e:
            await ctx.send("Invalid date or time must be in the form M-D-Y H:M:S" + " " + str(e))
            return
        
        thread = threading.Thread(target=self.timer, args=(ctx, timestamp, message,))
        thread.start()
        await ctx.send("Reminder Created!")