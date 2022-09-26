import discord

class InformationModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Please give a brief description of yourself.", style=discord.InputTextStyle.paragraph))
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
        self.stop()

    def get_user_description(self):
        return self.children[0].value