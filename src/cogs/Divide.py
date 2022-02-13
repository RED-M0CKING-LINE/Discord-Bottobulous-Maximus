from discord.ext import commands
import asyncio


class cogDivide(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()
        
    #FIX `divide 1 400000 outputs .25000 WHY
    @commands.command('divide')
    async def divide(self, ctx, *args):
        if not self.lock:
            await ctx.send('Im busy doing another calculation right now')
            return
        async with self.lock:
            try:
                steps = int(args[2])
                sigFig = 10 ** steps
            except IndexError:
                steps = 10
                sigFig = 10 ** steps

            try:
                top = float(args[0]) * sigFig
                bot = float(args[1])
            except ValueError:
                await ctx.send('no.')
                return
            except OverflowError:
                await ctx.send('Overflow error. Likely you put in too large of a integer for the significant figures. Largest value is 307')
                return

            invert = 1

            if bot == 0:
                await ctx.send("Don't pull that shit, buddy. Dividing by zero is no fucking joke. Are you TRYING to collapse the universe?")
                return None
            elif top < 0:
                invert = -invert
            elif bot < 0:
                invert = -invert
            res = (invert * ((top - 1) // bot + 1))
            if res > (8 ^ 99999) * sigFig:
                await ctx.send('Converting the number. This may take a moment...')
            res = '%d' % res #TODO this line converts the float to an int and if its too large it wont do it. i forgot why i added this line but there is a reason. "ValueError: cannot convert float NaN to integer"
            res = list(res)
            res.insert(-steps, '.')
            tmp = ''
            for i in res:
                tmp = tmp + i

            await ctx.send(tmp)

def setup(bot): # call this in main.py: bot.load_extension('cogs.Divide')
    bot.add_cog(cogDivide(bot))
