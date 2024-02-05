import discord

from commands.command import Command
from random import choice

responses = [
    "Console: Couldn't extend your reservation: you can only extend when there's less than 1 hour"
    + "left and no one else has booked the server.",
    "Console: Extended your reservation by 20 minutes",
    "Console: Extended your reservation by 60 minutes"
]


async def extend(msg: discord.Message, _):
    await msg.channel.send(choice(responses))


extend = Command("extend", "`: Tries to extend the reservation", extend)
