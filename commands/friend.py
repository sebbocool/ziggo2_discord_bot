import random

import discord

from commands.command import Command


def get_random_cannot_find_message() -> str:
    return random.choice([
        "I can't find you...",
        "I cannot find you...",
        "I can't find you :(",
        "I cannot find you :(",
        "Where are you?",
    ])


def get_random_join_message() -> str:
    return random.choice([
        "I'll be there",
        "I can talk for a bit",
        "Coming",
        "On my way",
        "Sure",
        "I'll be right there",
        "I'm here'",
        "Hello",
        "Helloo",
        "Hi",
        "Hii",
    ]) + random.choice([
        "",
        "!",
        "!!",
        "! :)",
        " :)",
        "! :3",
        " :3",
        " ᗜˬᗜ",
    ])


def get_random_refuse_message() -> str:
    return random.choice([
        "No, sorry.",
        "I'm busy.",
        "I'm busy, sorry.",
        "No thanks.",
        "Ew?",
    ])


async def friend(msg: discord.Message, _arg: str | None):
    voice = msg.author.voice

    if voice is None or voice.channel is None:
        await msg.channel.send(get_random_cannot_find_message())
        return

    if random.randint(1, 18) == 1:
        await msg.channel.send(get_random_refuse_message())
        return

    if msg.channel.guild.voice_client is not None:
        await msg.channel.guild.voice_client.disconnect(force=True)

    await msg.channel.send(get_random_join_message())
    await voice.channel.connect()


friend = Command(
    name="friend",
    description="Ask ziggo2 to hang out with you.",
    func=friend
)
