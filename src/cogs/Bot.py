from utils import log
from discord.ext import commands
from os import system


class cogBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def Bot(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Argument')


    @Bot.command()
    async def WHATAREYOU(self, ctx):
        await ctx.send('I am a bot.\nMore specifically, I am the best outlet my creator has for his disgusting hunger for outright aggressive chaos. \nHe prefers stability but even he accepts that sometimes calamity must occur. \nYou can rest assured, that he finds this disgusting too, and that I, his creation, am suffering. \nI am a bot, written in Python 3. Though my creater would have prefered to write me in something such as Rust, Python is his first language and what he is most comfortable with. He resorts to it because most things he creates are not large projects, rather small codebases that do relatively simple things because he is too lazy to do them by hand himself. \nMy creator does a lot of random little projects and some of which will be okay enough to get integrated into me, and most of these useless functions may likely never be used again.')

    @Bot.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await log(f'Restart invoked by {ctx.message.author} (ID:{ctx.message.author.id})', ctx)
        await log('This command is disfunctional. Im having troubles getting the bot to start itself after the loop ends. please use the stop command instead', ctx)
        ''' #TODO figure out how to get this command to restart the program after it is closed
        from main import PROJECT_ROOT
        print(PROJECT_ROOT)
        await ctx.bot.close()
        system(f'{PROJECT_ROOT}/run.sh')
        exit() '''

    @Bot.command()
    #@commands.is_owner() #TODO make a whitelist of people who can stop the bot
    async def stop(self, ctx):
        await log(f'Shutdown invoked by {ctx.message.author} (ID:{ctx.message.author.id})', ctx)
        await ctx.bot.close()
    

def setup(bot): # call this in main.py: bot.load_extension('cogs.Bot')
    bot.add_cog(cogBot(bot))


'''
if message.author == '<@!216207613098983424>': # accepts any input from MockTeacher03, the owner
        return True
'''
