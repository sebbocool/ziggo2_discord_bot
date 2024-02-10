import random
import asyncio

import discord

from commands.command import Command


async def mge(msg: discord.Message, arg: str | None):
    target = get_random_target() if arg is None else arg
    author = msg.author.mention
    arena, max_score = get_random_arena()

    await msg.channel.send(f"{author} joins arena {arena}.")
    await asyncio.sleep(0.5)
    await msg.channel.send(f"{target} joins arena {arena}.")
    await asyncio.sleep(1.0)

    won_by_author = random.choice([True, False])
    winner, loser = (author, target) if won_by_author else (target, author)
    loser_score = random.randint(0, max_score - 1)

    await msg.channel.send(f"{winner} (Score:{max_score}) defeats {loser} (Score:{loser_score}) " +
                           f"in duel to {max_score} on {arena}.")


def get_random_target() -> str:
    return random.choice([
        "B4nny",
        "Habib",
        "Arekk",
        "Blaze",
        "kaidus",
        "thalash",
        "Silentes"
        "Domo",
        "MGEMike",
        "GabeN",
        "Uncle Dane",
        "pablo.gonzalez2008",
        "OMEGATRONIC",
        "Donald J. Trump",
        "Joseph R. Biden",
    ])


def get_random_arena() -> (str, int):
    return random.choice([
        ("Viaduct Middle", 20),
        ("Granary Middle", 20),
        ("Granary Last", 20),
        ("Badlands Middle", 20),
        ("Badlands Spire", 20),
        ("Gullywash Middle", 20),
        ("Waste Middle", 20),
        ("Snakewater Middle", 20),
        ("Gravelpit C", 20),
        ("Process Middle", 20),
        ("Trainyard", 20),
        # ("Turris 1" , 20),
        # ("Turris 2", 20),
        # ("Ammomod", 20),
        ("Ammomod [MGE]", 20),
        # ("No Splash", 20),
        ("Endif", 5),
        # ("BBall 2v2", 20),
    ])


mge = Command(
    name="mge",
    arg="target",
    description="Fight someone in MGE",
    func=mge
)
