import time
import threading
from datetime import datetime

date_format = '%m-%d-%Y %H:%M:%S'
example = '06-25-2023 13:00:00'






async def timer(ctx, timeup, message):
    while True:
        if time.time() >= timeup:
            await ctx.send("@everyone " + message)
            return


def startReminder(ctx, timestamp, timer_message):

    t = threading.Thread(target=timer, args=(ctx, timestamp, timer_message))
    t.start()

def convertToTimestamp(date_string):
    #Turn date and time string into a datetime object
    date_time = datetime.strptime(date_string, date_format)
    # Convert the datetime object to a timestamp
    timestamp = datetime.timestamp(date_time)
    return timestamp

def startTimer(date_string, timer_message="Default", ):
