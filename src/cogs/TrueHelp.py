from discord.ext import commands
import asyncio
import subprocess


#TODO return the current working directory as well before listing the files
#TODO separate the directories and files
#FIXME if you run "`truehelp cogs/TrueHelp.py" the output will be broken. escape the '`' symbol maybe?

class cogTrueHelp(commands.Cog):

    def __init__(self, bot):
        self.lock = asyncio.Lock()
        self.bot = bot
    
    '''
    This truly helps the user...
    '''
    @commands.command(name='trueHelp') #FIXME the box includes the pycache directory. don't do that.
    async def run(self, ctx, *args):
        async with self.lock:
            try:
                if not str(args[0]).find('Data/') == -1 or not str(args[0]).find('..') == -1:
                    await ctx.send('No.')
                else:
                    with open(str(args[0]), encoding="UTF-8") as x:
                        msg = '```python3\n'
                        lineCount = 1
                        for l in x:
                            if (len(msg) + len(l)) > 1990:
                                await ctx.send(str(msg) + '```')
                                await asyncio.sleep(0.8)
                                msg = '```python3\n'
                            
                            msg = msg + str(lineCount) + '  ' + l
                            lineCount += 1
                        await ctx.send(str(msg) + '```')

            except IndexError:
                await ctx.send('Please Select a file:\n{}'.format(subprocess.check_output(['ls', '-R'], universal_newlines='\n')))
            except FileNotFoundError:
                await ctx.send('File does not exist.\nUsage: `trueHelp "cogs/TEMPLATE.py"')

def setup(bot): # call this in main.py: bot.load_extension('cogs.TrueHelp')
    bot.add_cog(cogTrueHelp(bot))
