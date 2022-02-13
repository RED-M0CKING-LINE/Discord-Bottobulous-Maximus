'''
NOTE crontab command for autostart: @reboot cd /root/Discord-Bottobulous-Maximus/src && /usr/bin/nohup /usr/bin/python3 /root/Discord-Bottobulous-Maximus/src/main.py  
TODO make it go in a docker container? maybe later 
'''

from discord.ext import commands
from discord.ext import tasks

from os import path

import utils

COMMAND_PREFIX = '`'
PROJECT_ROOT = path.dirname(__file__)
bot = commands.Bot(command_prefix=commands.when_mentioned_or(COMMAND_PREFIX), case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} (ID: {bot.user.id}) has connected.')
    print('Connected to the following guilds:')
    for guild in bot.guilds:
        print(f"    - {guild.name} (id: {guild.id})")
    print("#################### Ready.")


@bot.event
async def on_message(message):
    if utils.on_message_check(bot, message):
        await bot.process_commands(message) #TODO break processing if the message has been processed as a command


print('PROJECT_ROOT = ' + str(PROJECT_ROOT))

try: #TODO ensure this catches the errors it needs to. i havent tested it at all lmao
    with open("{}/../config/SECRETS/DISCORD_API_TOKEN".format(PROJECT_ROOT), "r") as f:
        TOKEN = f.readline()
        f.close()
except FileNotFoundError:
    print("No file for token at PROJECT_ROOT/../Data/DISCORD_API_TOKEN")
    exit()

#TODO autoadd all cogs in the folder dynamically and exclude a list of disabled (but installed cogs
enabled_cogs = ['Mention', 'TrueHelp', 'SimonSays', 'Divide', 'Everyone', 'Pin', 'FuckBryce', 'Spam', 'Bot'] # Disabled: 'Ping', 'Music',
for x in enabled_cogs:
    print('Loading Cog: ' + x)
    bot.load_extension('cogs.{}'.format(x))

bot.run(TOKEN)

