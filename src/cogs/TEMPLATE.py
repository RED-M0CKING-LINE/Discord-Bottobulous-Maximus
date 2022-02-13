import asyncio
from discord.ext import commands


class cogTEMPLATE(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()  # ensures that multiple instances of the command cannot be initiated in parallel
        self.loopStop = False  # stops the program when true

    @commands.group()
    async def TEMPLATE(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Argument')

    @TEMPLATE.command()
    async def stop(self, ctx):
        self.loopStop = True
        await ctx.send('Stopping TEMPLATE.')

    @TEMPLATE.command()
    async def start(self, ctx):
        async with self.lock:
            while True:
                if not self.loopStop:
                    await ctx.send('TEMPLATE')
                else:
                    self.loopStop = False
                    break

def setup(bot): # call this in main.py: bot.load_extension('cogs.TEMPLATE')
    bot.add_cog(cogTEMPLATE(bot))
