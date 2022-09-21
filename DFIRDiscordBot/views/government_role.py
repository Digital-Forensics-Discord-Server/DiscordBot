import discord
import json


def load_gov_data():
    with open("data/government.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    print(f"Loaded {len(data)} Government roles")
    return data

government_roles = load_gov_data()


class GovernmentRoleDropdown(discord.ui.Select):
    def __init__(self):
        MAX_DROPDOWN = 25
        options = []
        for role in government_roles[:MAX_DROPDOWN]:
            options.append(discord.SelectOption(
                label=role["role_name"],
                description=role["description"],
                emoji=role["flag_emoji"]
            ))
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
