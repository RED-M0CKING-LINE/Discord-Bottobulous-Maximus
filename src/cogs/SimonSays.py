from discord.ext import commands
import asyncio
from requests import get as WGET


class cogSimonSays(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()
        self.speak = False

    @commands.command(name='simonSpeaks')
    async def speak(self, ctx, *args):
        self.speak = True
        await self.run(ctx, args)

    @commands.command(name='simonSays')
    async def say(self, ctx, *args):
        await self.run(ctx, args)

    #TODO is this blocking? too tired to check now but make sure it doesnt stop program loop
    async def run(self, ctx, arg): #TODO make a way to stop this
        async with self.lock:
            if str(arg[0]).upper() == 'FILE':
                x = WGET(ctx.message.attachments[0].url).content.decode().split(' ')
                msg = ' '.join(x)
            else: 
                msg = ' '.join(arg)
                if '@everyone' in msg:
                    await ctx.send('Don\'t `@everyone`.')
                    return
                x = arg

            if len(msg) > 2000:
                msg = ''
                for l in x:
                    if (len(msg) + len(l)) > 1998:
                        await ctx.send(str(msg), tts = self.speak)
                        await asyncio.sleep(0.8)
                        if self.speak:
                            await asyncio.sleep(20)
                        msg = ''
                    msg = msg + ' ' + l
            await ctx.send(str(msg), tts=self.speak)
            self.speak = False

def setup(bot): # call this in main.py: bot.load_extension('cogs.SimonSays')
    bot.add_cog(cogSimonSays(bot))
    