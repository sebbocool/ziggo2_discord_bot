from typing import Callable, Coroutine

import discord

type CommandFunction = Callable[[discord.Message, str | None], Coroutine]


class Command:
    def __init__(self, name: str, description: str, func: CommandFunction):
        self.name = name
        self.description = description
        self.func = func

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    async def run(self, msg: discord.Message, arg: str | None):
        await self.func(msg, arg)
