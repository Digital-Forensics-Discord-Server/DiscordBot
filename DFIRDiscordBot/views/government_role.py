import discord


class GovernmentRoleDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="UK",
                description="Employee of a UK Government Agency",
                emoji='🇬🇧',
            ),
            discord.SelectOption(
                label="USA",
                description="Employee of a Federal or State agency",
                emoji='🇺🇸',
            ),
        ]
        super().__init__(
            placeholder="Select Country",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        self.view.stop()


class GovernmentRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.dropdown_view = GovernmentRoleDropdown()
        self.add_item(self.dropdown_view)
    
    def get_selection(self):
        return self.dropdown_view.values[0]
