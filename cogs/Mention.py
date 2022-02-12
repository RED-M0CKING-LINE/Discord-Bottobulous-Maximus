from discord.ext import commands
import asyncio


class cogMention(commands.Cog):
    stop = False  # stops the program when true
    #TODO mention stop didnt stop the bot at one point
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def mention(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('mention start <id> <repeat> <delay> \nmention stop')

    @mention.command(name='stop')
    async def stopper(self):
        self.stop = True

    '''
    `mention <id> <repeat> <delay>
    id: the users ID. enable developer mode to copy
    repeat: amount of times to repeat
    delay: amount of time to delay the sending of messages. default is a steady stream of chaos
    '''
    @mention.command(name='start')
    async def run(self, ctx, *args):
        try:
            repeat = int(args[1])
        except IndexError:
            repeat = 1
        try:
            sleep = int(args[2])
        except IndexError:
            sleep = 0.8
        if args[0] == '216207613098983424':
            await ctx.send('Get fucked nerd. LMFAO')
            return None
        elif not len(args[0]) == 18: #TODO add a check to make sure this contains no letters
            await ctx.send('Invalid ID. Let me know if you find a discord ID that isnt 18 characters or contain letters lmao')
        repeat = repeat -1
        loop = 0
        while loop <= repeat:
            loop += 1
            if self.stop:
                self.stop = False
                break
            await ctx.send('<@{}>'.format(args[0]))
            await asyncio.sleep(sleep)

def setup(bot): # call this in main.py: bot.load_extension('cogs.Mention')
    bot.add_cog(cogMention(bot))    
