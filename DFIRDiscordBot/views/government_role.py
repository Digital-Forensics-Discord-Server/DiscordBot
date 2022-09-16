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
        role_name = f"Government [{self.values[0]}]"
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role:
            await interaction.user.add_roles(role, reason="Bot role update")
            await interaction.response.send_message(
                f'Your roles have been updated to: {role_name}'
            )
        else:
            print(f"Unable to get Role for {role_name}")


class GovernmentRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(GovernmentRoleDropdown())
