from DFIRDiscordBot.views.general_role import GeneralRoleDropdownView
from discord.ext import commands, pages

import discord

class DFIRCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="updateroles", description="Update DFIR server role(s)")
    async def command_update_roles(self, ctx):
        await ctx.send_response("Please select your role", view=GeneralRoleDropdownView(), ephemeral=True)

def setup(bot):
    bot.add_cog(DFIRCommands(bot))