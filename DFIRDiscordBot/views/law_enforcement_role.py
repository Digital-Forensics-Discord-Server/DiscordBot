import discord


class LawEnforcementRoleDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Albania",
                description="Member of Albanian Federal/Municipal Police",
                emoji='🇦🇱',
            ),
            discord.SelectOption(
                label="Argentina",
                description="Member of Argentinian Federal/Provicial/Local Police",
                emoji='🇦🇷',
            ),
            discord.SelectOption(
                label="Australia",
                description="Member of Australian Federal/State Police",
                emoji='🇦🇺',
            ),
            discord.SelectOption(
                label="Austria",
                description="Member of Austrian Federal/State Police",
                emoji='🇦🇹',
            ),
            discord.SelectOption(
                label="Bangladesh",
                description="Member of the Bangladesh Police",
                emoji='🇧🇩',
            ),
            discord.SelectOption(
                label="Belgium",
                description="Member of Belgium Federal/Local Police",
                emoji='🇧🇪',
            ),
            discord.SelectOption(
                label="Bosnia",
                description="Member of the Bosnian Police",
                emoji='🇧🇦',
            ),
            discord.SelectOption(
                label="Brazil",
                description="Member of the Brazilian Federal/Civil/Municipal Police",
                emoji='🇧🇷',
            ),
            discord.SelectOption(
                label="Canada",
                description="Member of the Canadian Federal/Provincial/Municipal Police",
                emoji='🇨🇦',
            ),
            discord.SelectOption(
                label="Chile",
                description="Member of the Chilian Police",
                emoji='🇨🇱',
            ),
            discord.SelectOption(
                label="China",
                description="Member of the Chinese Police",
                emoji='🇨🇳',
            ),
            discord.SelectOption(
                label="Columbia",
                description="Member of the Colombian National Police",
                emoji='🇨🇴',
            ),
            discord.SelectOption(
                label="Croatia",
                description="Member of the Croatian Police",
                emoji='🇭🇷',
            ),
            discord.SelectOption(
                label="Cyprus",
                description="Member of the Cypriot Police",
                emoji='🇨🇾',
            ),
            discord.SelectOption(
                label="Czech Republic",
                description="Member of the Czech State/Municipal Police",
                emoji='🇨🇿',
            ),
            discord.SelectOption(
                label="Denmark",
                description="Member of the Danish Police",
                emoji='🇩🇰',
            ),
            discord.SelectOption(
                label="Dominican Republic",
                description="Member of the Dominican Republic's National Police",
                emoji='🇩🇴',
            ),
            discord.SelectOption(
                label="Estonia",
                description="Member of the Estonian Police and Border Guard",
                emoji='🇪🇪',
            ),
            discord.SelectOption(
                label="Finland",
                description="Member of the Finnish Police",
                emoji='🇫🇮',
            ),
            discord.SelectOption(
                label="France",
                description="Member of the French Police Nationale/Gendarmerie/Municipal Police",
                emoji='🇫🇷',
            ),
            discord.SelectOption(
                label="Germany",
                description="Member of German Federal/State/Municipal Police",
                emoji='🇩🇪',
            ),
            discord.SelectOption(
                label="Greece",
                description="Member of the Greek/Hellenic Police",
                emoji='🇬🇷',
            ),
            discord.SelectOption(
                label="Grenada",
                description="Member of the Royal Grenada Police Force",
                emoji='🇬🇩',
            ),
            discord.SelectOption(
                label="Iceland",
                description="Member of the Icelandic Police",
                emoji='🇮🇸',
            ),
            # discord.SelectOption(
            #     label="UK",
            #     description="Officer/Staff of a UK Police Force or NCA",
            #     emoji='🇬🇧',
            # ),
            # discord.SelectOption(
            #     label="USA",
            #     description="Sworn/Unsworn LE officer of a regional/state/federal LEA",
            #     emoji='🇺🇸',
            # ),
        ]
        super().__init__(
            placeholder="Select Country",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        role_name = f"Law Enforcement [{self.values[0]}]"
        role = discord.utils.get(interaction.guild.roles, name=role_name)
        if role:
            await interaction.user.add_roles(role, reason="Bot role update")
            await interaction.response.send_message(
                f'Your roles have been updated to: {role_name}'
            )
        else:
            print(f"Unable to get Role for {role_name}")


class LawEnforcementRoleDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(LawEnforcementRoleDropdown())
