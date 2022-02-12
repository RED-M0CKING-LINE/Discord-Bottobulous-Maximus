import utils
from discord.ext import commands


class cogSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pog(self, ctx):
        await ctx.send('pog')

    @commands.Cog.listener("on_message")
    async def on_message(self, message): #TODO convert these conditions into a config file so they are not hard coded and be changed easily. use keyword override and have a default setting at the top of the file defining all default values
        if not utils.on_message_check(self.bot, message): # stops the process if the check does not pass
            return
        msg_content = message.content.lower()
        if 'padoru' in msg_content:
            await message.channel.send('https://cdn.discordapp.com/attachments/897024945949913100/916812926281719818/9convert.com_-_padoru_padoru_1080pFHR.mp4.webm.mp4 ')
        elif 'pog' in msg_content:
            if 'pogger' in msg_content:
                if utils.rng(40):
                    await message.channel.send('https://cdn.discordapp.com/attachments/896254987200516147/909798898124595200/Poggers.mp4 ')
            else:
                await message.channel.send('Pog')
            return
        elif 'rick' in msg_content: # Rick roll
            if utils.rng(7):
                await message.channel.send('We\'re no strangers to love\nYou know the rules and so do I\nA full commitment\'s what I\'m thinking of\nYou wouldn\'t get this from any other guy\n\nI just wanna tell you how I\'m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nWe\'ve known each other for so long\nYour heart\'s been aching, but\nYou\'re too shy to say it\nInside, we both know what\'s been going on\nWe know the game and we\'re gonna play it\n\nAnd if you ask me how I\'m feeling\nDon\'t tell me you\'re too blind to see\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\n(Ooh, give you up)\n(Ooh, give you up)\nNever gonna give, never gonna give\n(Give you up)\nNever gonna give, never gonna give\n(Give you up)\n\nWe\'ve known each other for so long\nYour heart\'s been aching, but\nYou\'re too shy to say it\nInside, we both know what\'s been going on\nWe know the game and we\'re gonna play it\n\nI just wanna tell you how I\'m feeling\nGotta make you understand\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\n\nNever gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you\nhttps://www.youtube.com/watch?v=dQw4w9WgXcQ @everyone')
        elif 'owo' in msg_content:
            await message.channel.send('OwO')
        elif 'uwu' in msg_content:
            await message.channel.send('UwU')
        else:
            words = ['bussy', 'futa', 'lgbt', 'vore', 'loli', 'shota', 'sus', 'trap']
            for x in words:
                if ' ' + x.lower() in (' ' + message.content).lower():
                    await message.channel.send('stfu')
            return


def setup(bot): # call this in main.py: bot.load_extension("cogs.Spam")
    bot.add_cog(cogSpam(bot))
