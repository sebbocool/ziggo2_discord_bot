import discord

from bot import Ziggo2
from config import DISCORD_TOKEN


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    client = Ziggo2(intents=intents)
    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
