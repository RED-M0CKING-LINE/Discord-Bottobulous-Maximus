
from asyncio import sleep as async_sleep
import json
from random import random
from time import strftime, localtime, time_ns
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


async def sendMessage(ctx, message, maxCharacters=2000, maxMessages=30):  #TODO is ctx the right thing to pass here?
    ''' If you want to send a message and it MAY be longer than discords limit, 
    this will split it into multiple messages.
    ctx: this is the context of the message for the bot to reply into the same channel  #TODO make it so i can pass a channel argument to achieve the same purpose. passing the whole context is not needed
    message: string. this is the message to be sent
    maxCharacters: int. this is the maximum number of characters for each message to contain
    maxMessages: int. this is the maximum number of messages to send from the string, otherwise truncate the output. set to zero to allow any amount of messages
    '''
    lower = 0
    upper = maxCharacters
    sentMessages = 0
    while True:            
        if len(message) <= lower:
            break
        elif len(message) < upper:
            upper = len(message)
        await ctx.send(message[lower:upper])
        if maxMessages < sentMessages:
            await ctx.send('The output was too long and has been truncated to prevent grievous chat spam. The default threshold can be overridden if you so wish.')
        lower = lower + maxCharacters
        upper = upper + maxCharacters
        async_sleep(0.9)  # so that the bot does not get throttled as much  #FIXME ensure this works right. does this fix the blocking that happens when the bot is sending many messages? probably not



def getConfig(category, key):
    ''' This class will fetch you the config values stored in the specified category
    category: the group of values to search
    key: the value name to find
    Returns None if the key is not found
    '''
    with open('../config/config.json', 'r', encoding='UTF-8') as file:
        config = json.loads(file.read())
    try:
        return config[f"{category}"][f"{key}"]
    except KeyError:
        return None

def setConfig(category, key, value):
    ''' This class will store values into the config under a specific category
    category: the group of values to use
    key: the value name to set
    value: the stored value for the key. Values are stored exactly as they are passed in
    '''
    with open('../config/config.json', 'r', encoding='UTF-8') as file:
        config = json.loads(file.read())
    config.update({f"{category}": {f"{key}": value}})
    config = json.dumps(config)
    with open('../config/config.json', 'w', encoding='UTF-8') as file:
        file.write(config)
