import discord


class LawEnforcementRoleDropdown(discord.ui.Select):
    def __init__(self, page):
        if page == 1:
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
            ]
        elif page == 2:
            options = [
                discord.SelectOption(
                    label="India",
                    description="Member of the Indian Police Service",
                    emoji='🇮🇳',
                ),
                discord.SelectOption(
                    label="Indonesia",
                    description="Member of the Indonesian National Police/Municipal Police",
                    emoji='🇮🇩',
                ),
                discord.SelectOption(
                    label="Iran",
                    description="Member of the Law Enforcement Command of Islamic Republic of Iran",
                    emoji='🇮🇷',
                ),
                discord.SelectOption(
                    label="Iraq",
                    description="Member of the Iraqi Police",
                    emoji='🇮🇶',
                ),
                discord.SelectOption(
                    label="Ireland",
                    description="Member of the Garda Síochána",
                    emoji='🇮🇪',
                ),
                discord.SelectOption(
                    label="Israel",
                    description="Member of the Israeli Police",
                    emoji='🇮🇱',
                ),
                discord.SelectOption(
                    label="Italy",
                    description="Member of the Carabiniari/State/Provincial/Municipal Police",
                    emoji='🇮🇹',
                ),
                discord.SelectOption(
                    label="Jamaica",
                    description="Member of the Jamaica Constabulary Force",
                    emoji='🇯🇲',
                ),
                discord.SelectOption(
                    label="Japan",
                    description="Member of the Japanese National Police Agency",
                    emoji='🇯🇵',
                ),
                discord.SelectOption(
                    label="Korea",
                    description="Member of the Korean National Police Agency",
                    emoji='🇰🇷',
                ),
                discord.SelectOption(
                    label="Latvia",
                    description="Member of the State Police of Latvia",
                    emoji='🇱🇻',
                ),
                discord.SelectOption(
                    label="Lithuania",
                    description="Member of the Lithuanian Police Force",
                    emoji='🇱🇹',
                ),
                discord.SelectOption(
                    label="Luxembourg",
                    description="Member of the Grand Ducal Police",
                    emoji='🇱🇺',
                ),
                discord.SelectOption(
                    label="Malaysia",
                    description="Member of the Royal Malaysia Police",
                    emoji='🇲🇾',
                ),
                discord.SelectOption(
                    label="Maldives",
                    description="Member of the Maldives Police Force",
                    emoji='🇲🇻',
                ),
                discord.SelectOption(
                    label="Malta",
                    description="Member of the Malta Police Force",
                    emoji='🇲🇹',
                ),
                discord.SelectOption(
                    label="Mauritius",
                    description="Member of the Mauritius Police Force",
                    emoji='🇲🇺',
                ),
                discord.SelectOption(
                    label="Mexico",
                    description="Member of the Mexican Federal/State/Municipal Police",
                    emoji='🇲🇽',
                ),
                discord.SelectOption(
                    label="Monaco",
                    description="Member of the Public Security of Monaco",
                    emoji='🇲🇨',
                ),
                discord.SelectOption(
                    label="Mongolia",
                    description="Member of the Mongolian National Police Agency",
                    emoji='🇲🇳',
                ),
                discord.SelectOption(
                    label="Myanmar",
                    description="Member of the Myanmar Police Force",
                    emoji='🇲🇲',
                ),
                discord.SelectOption(
                    label="Nepal",
                    description="Member of the Nepalese Police Force",
                    emoji='🇳🇵',
                ),
                discord.SelectOption(
                    label="Netherlands",
                    description="Member of the Dutch Politie",
                    emoji='🇳🇱',
                ),
                discord.SelectOption(
                    label="New Zealand",
                    description="Member of the New Zealand Police",
                    emoji='🇳🇿',
                ),
            ]
        elif page == 3:
            options = [
                discord.SelectOption(
                    label="Spain",
                    description="Member of the Spanish Guardia Civil/Policia National/Policia Local",
                    emoji='🇪🇸',
                ),
                discord.SelectOption(
                    label="Sweden",
                    description="Member of the Swedish Police Authority",
                    emoji='🇸🇪',
                ),
                discord.SelectOption(
                    label="Switzerland",
                    description="Member of a Cantonal/Municipal Swiss Police Agency",
                    emoji='🇨🇭',
                ),
                discord.SelectOption(
                    label="Taiwan",
                    description="Member of the Taiwanese National Police Agency",
                    emoji='🇹🇼',
                ),
                discord.SelectOption(
                    label="Turkey",
                    description="Member of the General Directorate of Security/Gendarmerie",
                    emoji='🇹🇷',
                ),
                discord.SelectOption(
                    label="Ukraine",
                    description="Member of the National Police of Ukraine",
                    emoji='🇺🇦',
                ),
                discord.SelectOption(
                    label="United Arab Emirates",
                    description="Member of an Emirate's Police Force",
                    emoji='🇦🇪',
                ),
                discord.SelectOption(
                    label="UK",
                    description="Constable/Staff of a UK Police Force/NCA",
                    emoji='🇬🇧',
                ),
                discord.SelectOption(
                    label="Uruguay",
                    description="National Police of Uruguay",
                    emoji='🇺🇾',
                ),
                discord.SelectOption(
                    label="USA",
                    description="Sworn/Unsworn LE officer of a regional/state/federal LEA",
                    emoji='🇺🇸',
                ),
                discord.SelectOption(
                    label="Vietnam",
                    description="Member of the Vietnam People's Police",
                    emoji='🇻🇳',
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


class LawEnforcementRoleDropdownView(discord.ui.View):
    def __init__(self, page):
        super().__init__()
        self.dropdown_view = LawEnforcementRoleDropdown(page)
        self.add_item(self.dropdown_view)
    
    def get_selection(self):
        return self.dropdown_view.values[0]
