from DFIRDiscordBot.commands import DFIRCommands
from discord.ext import commands

class BotClient(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await self.add_cog(DFIRCommands(self))