from DFIRDiscordBot.client import BotClient
from DFIRDiscordBot.commands import DFIRCommands

import discord

class DFIRBot():
    def __init__(self, token):
        self.token = token

        self.intents = discord.Intents.default()
        # We need to read message contents
        self.intents.message_content = True
        # We need to be able to modify roles
        self.intents.members = True
        # Create the bot client
        self.client = BotClient(intents=self.intents, command_prefix='/')
    
    def run(self):
        # Run the bot
        self.client.run(self.token)