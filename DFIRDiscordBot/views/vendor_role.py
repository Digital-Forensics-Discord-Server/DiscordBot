import discord
import json


def load_vendor_data():
    with open("data/vendor.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    print(f"Loaded {len(data)} Vendor roles")
    return data

vendor_roles = load_vendor_data()


class VendorRoleDropdown(discord.ui.Select):
    def __init__(self):
        MAX_DROPDOWN = 25
        options = []
        for role in vendor_roles[:MAX_DROPDOWN]:
            options.append(discord.SelectOption(
                label=role["role_name"],
                description=role["description"]
            ))

        super().__init__(
            placeholder="Select Vendor",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        self.view.stop()


class VendorRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.dropdown_view = VendorRoleDropdown()
        self.add_item(self.dropdown_view)

    def get_selection(self):
        return self.dropdown_view.values[0]
