'''
NOTE crontab command for autostart: @reboot cd /root/Discord-Bottobulous-Maximus/src && /usr/bin/nohup /usr/bin/python3 /root/Discord-Bottobulous-Maximus/src/main.py > /root/BotCronAutorun.log
TODO make it go in a docker container? maybe later 
'''
global PROGRAM_START_TIME

from discord.ext import commands

from os import path
from utils import log, on_message_check as utils_on_message_check

log('Imports complete. Program starting.')

COMMAND_PREFIX = '`'
PROJECT_ROOT = path.dirname(__file__)
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), case_insensitive=True)

@bot.event
async def on_ready():
    log(f'{bot.user} (ID: {bot.user.id}) has connected.')
    log('Connected to the following guilds:')
    for guild in bot.guilds:
        log(f"    - {guild.name} (id: {guild.id})")
    log('Ready.')


@bot.event
async def on_message(message):
    if utils_on_message_check(bot, message):
        await bot.process_commands(message) #TODO break processing if the message has been processed as a command


log('PROJECT_ROOT = ' + str(PROJECT_ROOT))

try:
    with open("{}/../config/SECRETS/DISCORD_API_TOKEN".format(PROJECT_ROOT), "r") as f:
        TOKEN = f.readline()
        f.close()
except FileNotFoundError as e:
    log(str(e))
    log("No file for token at PROJECT_ROOT/../config/SECRETS/DISCORD_API_TOKEN")
    raise e

#TODO autoadd all cogs in the folder dynamically and exclude a list of disabled (but installed cogs
enabled_cogs = ['Mention', 'TrueHelp', 'SimonSays', 'Divide', 'Everyone', 'Pin', 'FuckBryce', 'Spam', 'Bot'] # Disabled: 'Ping', 'Music',
for x in enabled_cogs:
    log('Loading Cog: ' + x)
    bot.load_extension('cogs.{}'.format(x))  #BUG catch the exceptions this call throws and log them

log('Bot Initalized. Starting...')
bot.run(TOKEN) # THIS IS BLOCKING
log('Bot Stopped')
