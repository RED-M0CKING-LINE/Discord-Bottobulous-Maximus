# Much of this cog is taken from Rapptz because im kinda lazy. https://github.com/Rapptz/discord.py/blob/master/examples/basic_voice.py

import youtube_dl

import asyncio
import discord
from discord.ext import commands



'''TODO PROBLEMS WITH THIS COG
- it predownloads videos because streaming them is unstable. is there a way to get streaming to work right?
- predownloading large videos takes obnoxiously long. is there a way to make it go faster? (its at like 1000kbps rn)
- it does not purge old downloaded videos to save disk space.
- there is no queue system for videos. allow for a queue of 30 videos
- the bot wont autoleave the chat if there are no videos playing. this will be trivial to implement after a queue is made
- can it play playlists?
- set a pause/play option
- show a progress bar for downloading videos rather than just typing
- 
'''



# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'worstaudio/worst',
    'outtmpl': 'tmp/%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

maximum_video_length = 36100  # Max length in seconds

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        if 'duration' in data:
            if data['duration'] > maximum_video_length:
                return None # VIDEO IS TOO LONG

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class cogMusic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()  # ensures that multiple instances of the command cannot be initiated in parallel

    @commands.group(case_insensitive=True)
    async def Music(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Argument')

    @Music.command()
    async def stop(self, ctx):
        await ctx.send('Stopping Music.')
        await ctx.voice_client.disconnect()


    @Music.command()
    async def play(self, ctx, *, url):
        await self.ensure_voice(ctx)
        async with ctx.typing():
            player = await YTDLSource.from_url(url, loop=self.bot.loop)
            ctx.voice_client.play(player, after=lambda e: print(f'Player error: {e}') if e else None)

        await ctx.send(f'Now playing: {player.title}')


    

    ''' Call before any playing action
    '''
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
                raise commands.CommandError("Author not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()



def setup(bot): # call this in main.py: bot.load_extension('cogs.Music')
    bot.add_cog(cogMusic(bot))
