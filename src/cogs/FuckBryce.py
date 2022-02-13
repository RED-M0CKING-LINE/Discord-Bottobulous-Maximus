import asyncio
from random import randint
from time import sleep
from discord.ext import commands


class cogFuckBryce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lock = asyncio.Lock()
        self.loopStop = False  # stops the program when true
        
        self.delay = 0.9
        self.command_prefix = "!" # command prefix for the bot this cog controls
        self.commands_base = ["shove", "slap", "ringloss", "givering", "spring", "welp", "cng", "noway", "pog", "rainbow", "badnik", "bumper", 
                                "ice", "star", "spotlight", "ohno", "big", "small", "reallybig", "demon", "eggbox", "touchfluffy", "getdizzy"]
        self.commands_music = ["play ", "bs", "boss1", "boss2", "bossf", "bosshbh", "bossmini", "puyo", "cpz1", "cpz2", "credits", "erz1",
                                "erzp", "em", "ghz1", "ghz2", "hbhm", "hcz1", "hcz2", "lrz1", "lrz2", "mmz1", "mmz2", "metal", "msz1", "mszk", 
                                "msz2", "ooz1", "ooz2", "pinball", "psz1", "psz2", "ssz1", "ssz2", "spz1", "spz2", "super", "tmz1", "tmz2", 
                                "ufo", "ssz1", "ssz1", "aiz1", "RTW", "END", "CYF", "SSR", "MN1", "LNL", "SD", "FB", "INF", "DBM", "IAM", 
                                "SNZ", "PKH", "KTR", "DDZ", "MIKU", "SMU", "MCZ", "PIZZA", "FGB", "SST", "UBT", "ITW", "WIM"]
        self.commands_player = ["switch ", "Sonic", "Tails", "Knuckles", "Ray", "Amy"]
        self.commands_partner = ["partner ", "Sonic", "Tails", "Knuckles", "Ray", "Amy"]
        self.commands_shields = ["", "fire", "water", "thunder", "normal"]
        
    @commands.group()
    async def FuckBryce(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid Argument')

    @FuckBryce.command()
    async def stop(self, ctx):
        self.loopStop = True
        await ctx.send('Stopping FuckBryce.')

    @FuckBryce.command()
    async def start(self, ctx):
        async with self.lock:
            while True:
                if not self.loopStop:
                    string = self.command_prefix + self.pick_command() + "\n"
                    await ctx.send(string)
                    sleep(self.delay)
                else:
                    self.loopStop = False
                    break
    
    def pick_command(self):
        weight = len(self.commands_base)*2 -2 + 4
        command = randint(0, weight)
        test = 0
        try:
            try: # for some reason whenever command is 4 it is an invalid value and causes a "FUCKING ERROR" at the end of this function
                final = self.commands_base[command]
            except IndexError:
                command = command - len(self.commands_base)
                final = self.commands_base[command]
        except IndexError:
            command = command - len(self.commands_base) + 1
            if command == 0:
                command = randint(1, len(self.commands_shields) -2)
                final = self.commands_shields[0] + self.commands_shields[command]
            elif command == 1:
                command = randint(1, len(self.commands_partner) -2)
                final = self.commands_partner[0] + self.commands_partner[command]
            elif command == 2:
                command = randint(1, len(self.commands_player) -2)
                final = self.commands_player[0] + self.commands_player[command]
            elif command == 3:
                command = randint(1, len(self.commands_music) -2)
                final = self.commands_music[0] + self.commands_music[command]
            else:
                print(f"FUCKING ERROR! command VAR IS {str(command)} from the {str(test)} group")
                final = "message GOD FUCKING DAMN IT"
        return final
def setup(bot): # call this in main.py: bot.load_extension("cogs.FuckBryce")
    bot.add_cog(cogFuckBryce(bot))
