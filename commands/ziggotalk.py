from random import choice
from .command import Command

async def ziggo_quote(msg):
    quote = get_ziggo_quote()
    await msg.channel.send(quote, reference=msg)

def get_ziggo_quote():
    with open("ziggoquotes.txt", "r") as file:
        quotes = file.readlines()
        quote = "ziggokill: " + choice(quotes).strip()
    return quote

ziggotalk = Command("ziggotalk", "`: Need some motivation? Get a real quote from one of ziggo's logs.", ziggo_quote)