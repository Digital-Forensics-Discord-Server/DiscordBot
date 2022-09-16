import discord


class VendorRoleDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="AboutDFIR",
                description="A contributor to AboutDFIR"
            ),
            discord.SelectOption(
                label="Amped Software",
                description="An employee of Amped Software"
            ),
            discord.SelectOption(
                label="Binalyze",
                description="An employee of Binalyze"
            ),
            discord.SelectOption(
                label="Cellebrite",
                description="An employee of Cellebrite"
            ),
            discord.SelectOption(
                label="Data Analyzers LLC",
                description="An employee of Data Analyzers LLC"
            ),
            discord.SelectOption(
                label="Forensafe",
                description="An employee of Forensafe"
            ),
            discord.SelectOption(
                label="Forensic Focus",
                description="An employee of Forensic Focus"
            ),
            discord.SelectOption(
                label="GetData",
                description="An employee of GetData"
            ),
            discord.SelectOption(
                label="Hashcat",
                description="A maintainer of Hashcat"
            ),
            discord.SelectOption(
                label="Hexordia",
                description="An employee of Hexodria"
            ),
            discord.SelectOption(
                label="Magnet Forensics",
                description="An employee of Magnet Forensics"
            ),
            discord.SelectOption(
                label="MSAB",
                description="An employee of MSAB"
            ),
            discord.SelectOption(
                label="SANS Forensics Institute",
                description="An employee of SANS Forensics Institute"
            ),
            discord.SelectOption(
                label="Sumuri",
                description="An employee of Sumuri"
            ),
            discord.SelectOption(
                label="TCS Forensics",
                description="An employee of TCS Forensics"
            ),
        ]
        super().__init__(
            placeholder="Select Vendor",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'Please wait for a member of the moderation team to get in touch to verify your employment with {self.values[0]}'
        )


class VendorRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(VendorRoleDropdown())
