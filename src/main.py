'''
NOTE crontab command for autostart: @reboot cd /root/Discord-Bottobulous-Maximus/src && /usr/bin/nohup /usr/bin/python3 /root/Discord-Bottobulous-Maximus/src/main.py > /root/BotCronAutorun.log
TODO make it go in a docker container? maybe later 
'''

import asyncio
from time import sleep
from discord.ext import commands
from os import path
import utils

log = utils.log  #FIXME this is because i had to change the imports and i don't wish to rename all instances of this at the moment
log('main.py imports complete. Program starting.')

PROJECT_ROOT = path.dirname(__file__)  #TODO store into config rather than a variable
# '''

class Main:
    ''' This is the main program loop
    It runs the program. Sometimes restarting it.
    '''
    
    def __init__(self):
        log('PROJECT_ROOT = ' + str(PROJECT_ROOT))

        self.COMMAND_PREFIX = '`'  #TODO make this configurable
        #self.bot = commands.Bot(command_prefix=commands.when_mentioned_or(self.COMMAND_PREFIX), case_insensitive=True)
        self.__create_bot_object()

        try:  # Get the Discord API Token from its configured location
            with open("{}/../config/SECRETS/DISCORD_API_TOKEN".format(PROJECT_ROOT), "r") as f:
                self.TOKEN = f.readline()
                f.close()
        except FileNotFoundError as e:
            log(str(e))
            log("No file for token at PROJECT_ROOT/../config/SECRETS/DISCORD_API_TOKEN")
            raise e

        @self.bot.event #TODO make these methods private methods
        async def on_ready():
            log(f'{self.bot.user} (ID: {self.bot.user.id}) has connected.')
            log('Connected to the following guilds:')
            for guild in self.bot.guilds:
                log(f"    - {guild.name} (id: {guild.id})")
            log('Ready.')
    
        @self.bot.event
        async def on_message(message):
            if utils.on_message_check(self.bot, message):
                await self.bot.process_commands(message)
                return
        
        log('Bot Initalized.')
        
    def __create_bot_object(self):
        self.bot = commands.Bot(command_prefix=commands.when_mentioned_or(self.COMMAND_PREFIX), case_insensitive=True)

    def enable_cogs(self):
        #TODO autoadd all cogs in the folder dynamically and exclude a list of disabled (but installed cogs
        enabled_cogs = ['Mention', 'TrueHelp', 'SimonSays', 'Divide', 'Everyone', 'Pin', 'FuckBryce', 'Spam', 'Bot'] # Disabled: 'Ping', 'Music',
        for x in enabled_cogs:
            log('Loading Cog: ' + x)
            self.bot.load_extension(f'cogs.{x}')  #BUG catch the exceptions this call throws and log them

    def run(self):
        self.enable_cogs()
        #try:
        self.bot.run(self.TOKEN)
        #self.bot.logout()
        self.bot.clear()

        '''
        except RuntimeError as e:
            timeout = 0
            while not self.bot.is_closed():
                sleep(.1)
                timeout += 1
                if timeout > 100: # sets timeout for program to close. for 10 seconds, write 100.
                    print('Timeout Exceeded.')
                    raise e
                    # '''

'''
async def main():
    Main().run() # '''

if __name__ == "__main__":
    while(True):
        utils.setConfig('runtime', 'restart', (True if utils.getConfig('user', 'AutoRestart') == True else False)) # Sets the default to not restart when the program closes #TODO read this from a config file of what the user prefers
        #try:
        Main().run()  # THIS IS BLOCKING
    #    asyncio.run(main())
        #except BaseException as e: #TODO make it catch any fatal exception from the program and log it
        #    log('{}'.format(e))

        if False == utils.getConfig('runtime', 'restart'):  #BUG this still wont restart the program. it will loop back to the start call but it errors out. something about loops not being closed. encapsulate entire program in a loop and delete all objects?, then reinitialize
            log('Bot Stopped.')
            break
        asyncio.set_event_loop(asyncio.new_event_loop())  # This line is the solution of much suffering when trying to have the bot restart itself
        sleep(1)

























