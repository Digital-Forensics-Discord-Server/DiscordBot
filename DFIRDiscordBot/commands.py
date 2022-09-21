from DFIRDiscordBot.views.general_role import GeneralRoleDropdownView
from DFIRDiscordBot.views.government_role import GovernmentRoleDropdownView
from DFIRDiscordBot.views.info_modal import InformationMobile
from DFIRDiscordBot.views.law_enforcement_role import LawEnforcementRoleDropdownView
from DFIRDiscordBot.views.vendor_role import VendorRoleDropdownView

from discord.ext import commands, pages

import discord

IGNORED_ROLES = [
    "Government",
    "Law Enforcement",
    "Vendor",
    "Moderators",
    "Contributor",
    "DFIR Author",
    "Nitro Booster",
    "@everyone",
]


class DFIRCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="updateroles", description="Update DFIR server role(s)")
    async def update_roles(self, ctx: discord.ApplicationContext):
        modal = InformationMobile(title="Welcome to the DFIR Discord Server")
        test = await ctx.send_modal(modal)
        await modal.wait()

        added_roles = []
        view = GeneralRoleDropdownView()
        interaction = await ctx.send_followup(
            "Please select the role which most describes your current experience and position within DFIR",
            view=view,
            ephemeral=True
        )
        await view.wait()
        
        for role in view.get_selections():
            added_roles.append(role)

        # If we've specified we're a vendor in one of our selected roles
        if "Vendor" in view.get_selections():
            vendor_view = VendorRoleDropdownView()
            await interaction.edit(
                content="Please select the Vendor you work for. Please note that this step requires additional verification with the Moderation team",
                view=vendor_view
            )
            await vendor_view.wait()

            import os
            mod_channel = discord.utils.get(ctx.guild.text_channels, name=os.getenv("MOD_CHANNEL_NAME"))
            if mod_channel:
                await mod_channel.send(f"User <@{ctx.user.id}> has requested the following Vendor role: {vendor_view.get_selection()}")

        # If we've specified we're law enforcement in one of our selected roles
        if "Law Enforcement" in view.get_selections():
            paginator = pages.Paginator(
                pages=[
                    pages.Page(
                        content="", custom_view=LawEnforcementRoleDropdownView(page=1)
                    ),
                    pages.Page(
                        content="", custom_view=LawEnforcementRoleDropdownView(page=2)
                    ),
                    pages.Page(
                        content="", custom_view=LawEnforcementRoleDropdownView(page=3)
                    ),
                ],
                loop_pages=False,
                show_indicator=True,
                default_button_row=1,
            )
            
            await paginator.respond(test, ephemeral=True)
            await paginator.wait()

            role_name = f"Law Enforcement [{paginator.pages[paginator.current_page].custom_view.get_selection()}]"
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                added_roles.append(role_name)
            else:
                print(f"Unable to get Role for {role_name}")
            added_roles.remove("Law Enforcement")

        # If we've specified we're government in one of our selected roles
        if "Government" in view.get_selections():
            gov_view = GovernmentRoleDropdownView()
            await interaction.edit(
                content="Please select the country you are a Government employee in",
                view=gov_view
            )
            await gov_view.wait()

            role_name = f"Government [{gov_view.get_selection()}]"
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                added_roles.append(role_name)
            else:
                print(f"Unable to get Role for {role_name}")
            added_roles.remove("Government")

        # Start by removing all current roles that user has
        for current_role in ctx.user.roles:
            if current_role.name in IGNORED_ROLES:
                continue
            await ctx.user.remove_roles(current_role)

        # Loop through the list of users and start assigning
        for selected_role in added_roles:
            if selected_role in IGNORED_ROLES:
                continue

            role = discord.utils.get(ctx.guild.roles, name=selected_role)
            if role:
                await ctx.user.add_roles(role, reason="Bot role update")
            else:
                print(f"Unable to get Role for {selected_role}")

        await interaction.edit(
            content=f'Your roles have been updated to: {", ".join(added_roles)}. If you specified a vendor, please wait for a member of the moderation team to get in touch to verify employment',
            view=None
        )

    @discord.slash_command(name="verify", description="This command is used to verify users in certain roles via email addresses")
    async def verify(self, ctx: discord.ApplicationContext):
        await ctx.send_response(content="This command will be used in future for optional email verification for Law Enforcement and vendors", ephemeral=True)
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged on as {self.bot.user}")
        activity = discord.Activity(
            type=discord.ActivityType.watching,
            name="the DFIR server",
        )
        await self.bot.change_presence(status=discord.Status.online, activity=activity)


def setup(bot):
    bot.add_cog(DFIRCommands(bot))
