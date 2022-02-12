from discord.ext import commands
import asyncio
import subprocess


class cogPing(commands.Cog):
    #stop = False  # stops the program when true
    #TODO impliment a stopper and a timeout for this command

    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()

    @commands.command(name='ping')
    async def ping(self, ctx, arg=2):
        if not self.lock:
            await ctx.send('I\'m busy running another ping command.')
            return
        async with self.lock:
            if arg > 100:
                arg = 100
            elif arg < 1:
                arg = 1
            await ctx.send('{}'.format(await subprocess.check_output(['ping', '-c', str(int(arg)), '1.1.1.1'], universal_newlines='\n').split('\n\n')[-1]))

def setup(bot): # call this in main.py: bot.load_extension('cogs.Ping')
    bot.add_cog(cogPing(bot))
