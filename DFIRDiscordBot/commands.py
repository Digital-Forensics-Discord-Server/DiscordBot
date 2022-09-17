from DFIRDiscordBot.views.general_role import GeneralRoleDropdownView
from DFIRDiscordBot.views.government_role import GovernmentRoleDropdownView
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
    async def command_update_roles(self, ctx: discord.ApplicationContext):
        added_roles = []

        view = GeneralRoleDropdownView()
        interaction = await ctx.send_response(
            "Please select your role", view=view, ephemeral=True
        )
        await view.wait()
        
        for role in view.get_selections():
            added_roles.append(role)

        # If we've specified we're a vendor in one of our selected roles
        if "Vendor" in view.get_selections():
            vendor_view = VendorRoleDropdownView()
            await interaction.edit_original_message(
                content="Please select the Vendor you work for. Please note that this step requires additional verification with the Moderation team",
                view=vendor_view
            )
            await vendor_view.wait()

            await interaction.response.send_message(
                f'Please wait for a member of the moderation team to get in touch to verify your employment with {vendor_view.get_selection()}',
                ephemeral=True
            )

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
            
            await paginator.respond(interaction, ephemeral=True)
            await paginator.wait()

            role_name = f"Law Enforcement [{paginator.pages[paginator.current_page].custom_view.get_selection()}]"
            role = discord.utils.get(interaction.guild.roles, name=role_name)
            if role:
                added_roles.append(role_name)
            else:
                print(f"Unable to get Role for {role_name}")

        # If we've specified we're government in one of our selected roles
        if "Government" in view.get_selections():
            gov_view = GovernmentRoleDropdownView()
            await interaction.edit_original_message(
                content="Please select the country you are a Government employee in",
                view=gov_view
            )
            await gov_view.wait()

            role_name = f"Government [{gov_view.get_selection()}]"
            role = discord.utils.get(interaction.guild.roles, name=role_name)
            if role:
                added_roles.append(role_name)
            else:
                print(f"Unable to get Role for {role_name}")

        # Start by removing all current roles that user has
        for current_role in interaction.user.roles:
            if current_role.name in IGNORED_ROLES:
                continue
            await interaction.user.remove_roles(current_role)

        # Loop through the list of users and start assigning
        for selected_role in added_roles:
            if selected_role in IGNORED_ROLES:
                continue

            role = discord.utils.get(interaction.guild.roles, name=selected_role)
            if role:
                await interaction.user.add_roles(role, reason="Bot role update")
            else:
                print(f"Unable to get Role for {selected_role}")

        await interaction.edit_original_message(
            content=f'Your roles have been updated to: {", ".join(added_roles)}. If you specified a vendor, please wait for a member of the moderation team to get in touch',
            view=None
        )


def setup(bot):
    bot.add_cog(DFIRCommands(bot))
