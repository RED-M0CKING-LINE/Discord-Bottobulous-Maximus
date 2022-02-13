
from random import random
from time import strftime, localtime

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


''' A command to log actions
if ctx is provided it will send the log to the discord chat where it was invoked as well

this is very minimal. create a rolling log maybe?
'''
async def log(text, ctx = None):
    text = strftime("%H:%M:%S", localtime()) + 'EST: ' + text
    if not ctx == None:
        await ctx.send('Log: ' + text)
    print(text)
