from discord.ext import commands
import asyncio


class cogEveryone(commands.Cog):
    stop = False  # stops the program when true

    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()

    @commands.group()
    async def everyone(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('@everyone')

    @everyone.command(name='stop')
    async def stopper(self):
        self.stop = True

    @everyone.command()
    async def start(self, ctx, arg=3):
        async with self.lock:
            repeat = arg -1
            tmp = 0
            while tmp <= repeat:
                tmp += 1
                await ctx.send('@everyone')

def setup(bot): # call this in main.py: bot.load_extension('cogs.Everyone')
    bot.add_cog(cogEveryone(bot))
