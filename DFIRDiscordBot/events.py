from discord.ext import commands

import discord


class DFIREvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged on as {self.bot.user}")
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="the DFIR server",
        )
        await self.bot.change_presence(status=discord.Status.online, activity=activity)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        print(f"{member} joined the server")
        new_members_role = discord.utils.get(
            member.guild.roles, name="New Members"
        )
        await member.add_roles(new_members_role, reason="Assigning New Members role upon join")
        await member.send("Welcome to the DFIR Discord Server! Use `/updateroles` in #role-assignment to start the role assignment process")


def setup(bot):
    bot.add_cog(DFIREvents(bot))
