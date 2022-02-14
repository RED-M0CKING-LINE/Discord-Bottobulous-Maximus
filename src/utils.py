
from random import random
from time import sleep, strftime, localtime, time_ns
from datetime import timedelta

#TODO make some code to show a progress bar message in chat and edit it based on the progress of an operation.

#TODO add a class in here that will handle reading all the configuration

'''
when you define an on_message event listener it will execute that listener and the main on_message event.
This is to be called in every on_message event listener before any processing is done, or else the bot may act unwantedly

returns true if the message is okay to be processed
'''
def on_message_check(bot, message):
    if message.author == bot.user:
        return False
    #elif message.author == '<@!342478084483579904>': # this should keep shiny from stopping the bot
    #    return False
    return True

'''
input the chance of something happening and it will return a boolean

chance: 0 to 100. represents percent of chance of returning true. None if chance is invalid
'''
def rng(chance):
    if 0 > chance or chance > 100:
        return None
    return random() <= chance/100

''' This calculates the uptime of the program in human readable format
'''
PROGRAM_START_TIME = time_ns()
def getUptime():
    return str(timedelta(microseconds=(time_ns() - PROGRAM_START_TIME)/1000))

''' Logging commands
asyncLog() will log to chat if ctx is passed, then calls log()
log() only logs to console and file  #TODO make log() log to a file as well
'''
def log(text):
    print(f"{getUptime()}: {str(text)}")
async def asyncLog(text, ctx = None):
    if not ctx == None:
        await ctx.send(f"Log: {getUptime()}: {str(text)}") #TODO test to make sure this works with "`bot stop"
    log(text)

'''
'''
async def sendMessage(ctx, string, maxCharacters=2000):
    lower = 0
    upper = maxCharacters
    while True:
        if len(string) <= lower:
            break
        elif len(string) < upper:
            upper = len(string)
        await ctx.send(string[lower:upper])
        lower = lower + maxCharacters
        upper = upper + maxCharacters
    sleep(.9) # so that the bot does not get throttled as much
