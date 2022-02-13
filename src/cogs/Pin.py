from discord.ext import commands

#TODO make it so people can just reply to a message to pin it (rather than copying the ID)


class cogPin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    async def getMessage(self, ctx, id: int):
        try:
            message_id = int(id)
            message = await ctx.fetch_message(message_id)
        except ValueError:
            message = None
            ctx.send('Invalid Message ID')
        return message

    @commands.command()
    async def pin(self, ctx, id: int):
        message = await self.getMessage(ctx, id)
        if not message == None:
            await message.pin()
            await ctx.send(f'Message {id} pinned by {ctx.message.author.mention}')

    @commands.command()
    async def unpin(self, ctx, id: int):
        message = await self.getMessage(ctx, id)
        if not message == None:
            await message.unpin()
            await ctx.send(f'Message {id} unpinned by {ctx.message.author.mention}')

def setup(bot): # call this in main.py: bot.load_extension('cogs.Pin')
    bot.add_cog(cogPin(bot))
