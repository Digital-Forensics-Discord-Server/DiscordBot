import discord
import json


def load_le_data():
    with open("data/law_enforcement.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    print(f"Loaded {len(data)} Law Enforcement roles")
    return data

law_enforcement_roles = load_le_data()


class LawEnforcementRoleDropdown(discord.ui.Select):
    def __init__(self, page):
        MAX_DROPDOWN = 25
        options = []
        for role in law_enforcement_roles[(page-1) * MAX_DROPDOWN:page * MAX_DROPDOWN]:
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


class LawEnforcementRoleDropdownView(discord.ui.View):
    def __init__(self, page):
        super().__init__()
        self.dropdown_view = LawEnforcementRoleDropdown(page)
        self.add_item(self.dropdown_view)
    
    def get_selection(self):
        return self.dropdown_view.values[0]
