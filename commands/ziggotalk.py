import random

import discord

from commands.command import Command


async def ziggo_quote(msg: discord.Message):
    quote = get_ziggo_quote()
    await msg.channel.send(quote, reference=msg)


def get_ziggo_quote():
    with open("resources/ziggoquotes.txt", "r") as file:
        quotes = file.readlines()
        quote = "ziggokill: " + random.choice(quotes).strip()
    return quote


ziggotalk = Command(
    name="ziggotalk",
    description="`: Need some motivation? Get a real quote from one of ziggo's logs.",
    func=ziggo_quote
)
