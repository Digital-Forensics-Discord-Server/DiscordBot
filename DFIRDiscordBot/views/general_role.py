import discord


class GeneralRoleDropdown(discord.ui.Select):
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
        await interaction.response.defer()
        self.view.stop()


class GeneralRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.dropdown_view = GeneralRoleDropdown()
        self.add_item(self.dropdown_view)

    def get_selections(self):
        return self.dropdown_view.values
