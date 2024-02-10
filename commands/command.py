from typing import Callable, Coroutine

import discord

type CommandFunction = Callable[[discord.Message, str | None], Coroutine]


class Command:
    def __init__(self, func: CommandFunction, name: str, description: str, arg: str | None = None):
        self.name = name
        self.description = description
        self.func = func
        self.arg_info = arg

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_arg_info(self) -> str | None:
        return self.arg_info

    async def run(self, msg: discord.Message, arg: str | None):
        await self.func(msg, arg)
