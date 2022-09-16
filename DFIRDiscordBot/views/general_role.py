from DFIRDiscordBot.views.government_role import GovernmentRoleDropdownView
from DFIRDiscordBot.views.law_enforcement_role import LawEnforcementRoleDropdownView
from DFIRDiscordBot.views.vendor_role import VendorRoleDropdownView

import discord


class GeneralRoleDropdown(discord.ui.Select):
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

    def __init__(self):
        options = [
            discord.SelectOption(
                label="Law Enforcement",
                description="Law Enforcement officer/staff who works in DFIR",
                emoji="👮"
            ),
            discord.SelectOption(
                label="Private Sector",
                description="DFIR-related private sector role",
                emoji="👨‍💼",
            ),
            discord.SelectOption(
                label="DFIR Student",
                description="A student in DFIR",
                emoji="🧑‍🎓"
            ),
            discord.SelectOption(
                label="Government",
                description="Government employee who works in DFIR",
                emoji="🏛️",
            ),
            discord.SelectOption(
                label="Vendor",
                description="Vendor of a DFIR product",
                emoji="🏢"
            ),
            discord.SelectOption(
                label="Public Sector",
                description="DFIR-related private sector role",
                emoji="🏛️",
            ),
            discord.SelectOption(
                label="DFIR Instructor",
                description="An instructor for a DFIR course",
                emoji="👨‍🏫",
            ),
            discord.SelectOption(
                label="DFIR Professor",
                description="A professor for an academic DFIR course",
                emoji="👨‍🏫",
            ),
            discord.SelectOption(
                label="DFIR Hobbyist",
                description="DFIR hobbyist"
            ),
            discord.SelectOption(
                label="Freelance",
                description="DFIR Freelancer"
            ),
            discord.SelectOption(
                label="DFIR Recruiter",
                description="DFIR Recruiter"
            ),
        ]

        super().__init__(
            placeholder="Select Role(s)", min_values=1, max_values=5, options=options
        )

    async def callback(self, interaction: discord.Interaction):
        # Start by removing all current roles that user has
        for current_role in interaction.user.roles:
            if current_role.name in self.IGNORED_ROLES:
                continue
            await interaction.user.remove_roles(current_role)

        # Loop through the list of users and start assigning 
        for selected_role in self.values:
            if selected_role in self.IGNORED_ROLES:
                continue
            
            role = discord.utils.get(interaction.guild.roles, name=selected_role)
            if role:
                await interaction.user.add_roles(role, reason="Bot role update")
            else:
                print(f"Unable to get Role for {selected_role}")
        
        interaction = await interaction.response.send_message(
            f'Your roles have been updated to: {", ".join(self.values)}',
            ephemeral=True
        )

        if "Vendor" in self.values:
            await interaction.followup.send(
                'Please select the Vendor you work for. Please note that this step requires additional verification with the Moderation team',
                view = VendorRoleDropdownView(),
                ephemeral=True
            )
        
        if "Law Enforcement" in self.values:
            await interaction.followup.send(
                'Please select the country you are a Law Enforcement officer / staff in',
                view = LawEnforcementRoleDropdownView(),
                ephemeral=True
            )
        
        if "Government" in self.values:
            await interaction.followup.send(
                'Please select the country you are a Government employee in',
                view = GovernmentRoleDropdownView(),
                ephemeral=True
            )


class GeneralRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(GeneralRoleDropdown())
