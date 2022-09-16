from DFIRDiscordBot.views.general_role import GeneralRoleDropdownView
from discord.ext import commands


class DFIRCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="updaterole")
    async def command_update_roles(self, ctx):
        await self.update_roles(ctx)

    @commands.command(name="updateroles")
    async def command_update_role (self, ctx):
        await self.update_roles(ctx)
        
    async def update_roles(self, ctx):
        await ctx.send("Please select your role", view=GeneralRoleDropdownView())