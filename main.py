from DFIRDiscordBot.bot import DFIRBot

import dotenv
import os

if __name__ == "__main__":
    # Load .env file
    dotenv.load_dotenv()

    # Run the bot
    bot = DFIRBot(os.getenv("BOT_TOKEN"))
    bot.run()