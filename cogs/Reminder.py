from discord.ext import commands
from discord import app_commands
import threading
import asyncio
import time
import re
from datetime import datetime, timedelta

class Reminder(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.date_format = '%m-%d-%Y %H:%M:%S'
        self.re_date = r'\d{2}-\d{2}-\d{4}'
        self.re_time = r'\d{2}:\d{2}:\d{2}'
        self.re_num =  r'^\d+$'
        self.re_alpha =  r'^[a-zA-Z]+$'
        #example = '06-25-2023 13:00:00'

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


    @app_commands.command(name="reminder", description="Sets a reminder")
    @app_commands.choices(time_unit=[
    app_commands.Choice(name='Minutes', value=1),
    app_commands.Choice(name='Hours', value=60),
    app_commands.Choice(name='Days', value=1440)])
    @app_commands.describe(message="What do you want the reminder to say?")
    @app_commands.describe(time_unit="The type of time unit")
    @app_commands.describe(how_many="The number of time_units from now to set the reminder")
    async def reminder(self, interaction, message:str, time_unit:app_commands.Choice[int], how_many:int):
        current_datetime = datetime.now()
        num_minutes = how_many * time_unit.value

        timer_time = current_datetime + timedelta(minutes=num_minutes)
        timer_timestamp = timer_time.timestamp()

        thread = threading.Thread(target=self.timer, args=(interaction, timer_timestamp, message,))
        thread.start()
        await interaction.response.send_message("Reminder Created!")



    @app_commands.command(name="reminder_complex", description="Sets a reminder with fine tuning of the time")
    @app_commands.describe(message="What do you want the reminder to say?")
    @app_commands.describe(days="The number of days from now to set the reminder")
    @app_commands.describe(hours="The number of hours from now to set the reminder")
    @app_commands.describe(minutes="The number of minutes from now to set the reminder")
    async def reminder_complex(self, interaction, message:str, days:int, hours:int, minutes:int):
        current_datetime = datetime.now()

        timer_time = current_datetime + timedelta(days=days, hours=hours, minutes=minutes)
        timer_timestamp = timer_time.timestamp()

        thread = threading.Thread(target=self.timer, args=(interaction, timer_timestamp, message,))
        thread.start()
        await interaction.response.send_message("Reminder Created!")



async def setup(bot):
    await bot.add_cog(Reminder(bot))
