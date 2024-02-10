import random
import asyncio

import discord

from commands.command import Command


async def bomba(msg: discord.Message, arg: str | None):
    target = "the Medic" if arg is None else arg

    author = msg.author.mention

    await msg.channel.send(f"{author} bombs {target}, and...")
    await asyncio.sleep(1)

    choices = [
        (10, f"{author} beefs."),
        (10, f"{author} fails his jump..."),
        (9, f"{author} misses his rockets..."),
        (9, f"{author} gets denied."),
        (8, f"{author} craters."),
        (8, f"{author} dies to a trap."),
        (8, f"{target} surfs away."),
        (7, f"{author} gets airshot!"),
        (7, f"{author} forces {target}!"),
        (7, f"{author} dies, but forces {target} nonetheless!"),
        (6, f"{author} gets airpiped!"),
        (6, f"{author} dominates {target}!"),
        (6, f"{target} pulls off a clutch save with the ÜberSaw!"),
        (6, f"{author} forces {target}, and gets out!"),
        (6, f"{author} misses, but {target} uses anyway!"),
        (5, f"{author} kills {target}! Looks like someone forgot to build."),
        (5, f"{target} hits a crossbow airshot!"),
        (5, f"{author} kills {target}! He was on Kritzkrieg all along!"),
        (5, f"{author} syncs his rockets! It's a force!"),
        (5, f"{author} misses {target}, but kills a Soldier instead!"),
        (5, f"{author} misses {target}, but kills a Scout instead!"),
        (4, f"{author} misses {target}, but kills the Demo instead!"),
        (4, f"{author} gets headshot mid air!"),
        (4, f"{author} airshots {target}! It's a force!"),
        (4, f"{target} lives on 1 HP."),
        (4, f"{target} gets forced by the team's spam."),
        (3, f"{author} is out of ammo?"),
        (3, f"{author} drops {target}!"),
        (3, f"{target} was hiding in the forward spawn..."),
        (3, f"{author} syncs his rockets! It's a drop!"),
        (2, f"{author} lost connection to the server!"),
        (2, f"{author} timed out."),
        (2, f"{author} airshots {target}! It's a drop!"),
        (2, f"{author} drops {target}, and kills them all!"),
        (1, f"{author} disconnected. (VAC banned from secured server)"),
    ]

    weights, population = zip(*choices)

    result = random.choices(population, weights)[0]

    await msg.channel.send(result)

bomba = Command(
    name="bomba",
    arg="target",
    description="Simulate a bomb, will you drop the medic or feed embarrassingly?",
    func=bomba
)
