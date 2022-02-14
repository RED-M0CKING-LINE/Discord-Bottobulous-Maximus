# I am not going to lie, this is probably my favorite cog so far

from discord.ext import commands
import asyncio
from decimal import Decimal, MAX_PREC, Context
from utils import sendMessage


class cogDivide(commands.Cog):  #TODO make this into a math function and allow it to add, subtract, multiply, and whatever else. all that should have to change is this line 'res = Context(prec=sigFig).divide(top, bot)'
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()
        
    @commands.command('divide')
    async def divide(self, ctx, *args, repeat=None):
        if not self.lock:
            await ctx.send('Im busy doing another calculation right now')
            return
        async with self.lock:
            if not repeat == None:
                if repeat > 100:
                    return
            try:
                sigFig = 100
                sigFig = int(args[2])
                if sigFig > MAX_PREC or sigFig == 0:
                    sigFig = MAX_PREC
                
            except IndexError:
                pass  # There is no problem. just use the default value
            except ValueError:
                await ctx.send('Remember, I cannot do math with letters!')
                return

            top = Decimal(args[0])
            bot = Decimal(args[1])
            try:
                res = Context(prec=sigFig).divide(top, bot)
            except MemoryError:
                sigFig = sigFig*.5
                await ctx.send(f"Memory Error. Trying again with {sigFig} significant figures.")
                if repeat == None:
                    repeat = 0
                asyncio.create_task(cogDivide.divide(self, ctx, top, bot, sigFig, repeat=repeat+1))
                return
            res = format(res, f'.{sigFig}f')  # puts it into a string and takes it out of scientific notation
            clean = False
            while not clean:
                if res[-1] == '0':
                    res = res[:-1]
                else:
                    clean = True
                    if res[-1] == '.':
                        res = res[:-1]
            await sendMessage(ctx, res)
            

def setup(bot): # call this in main.py: bot.load_extension('cogs.Divide')
    bot.add_cog(cogDivide(bot))
