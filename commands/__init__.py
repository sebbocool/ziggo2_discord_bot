import discord

from commands.ziggotalk import ziggotalk
from commands.bomba import bomba
from commands.pingziggo import pingziggo
from commands.translate import translate
from commands.extend import extend
from commands.help_command import help_command


COMMAND_PREFIX = "!"

all_commands = {}


def add_command(command, prefix=COMMAND_PREFIX) -> None:
    all_commands[prefix + command.get_name()] = command


add_command(ziggotalk)
add_command(bomba)
add_command(pingziggo)
add_command(translate)
add_command(extend, "!")
add_command(help_command)


async def run_command(message: discord.Message):
    name, *arg = message.content.strip().split(" ", 1)
    if name in all_commands:
        arg = arg[0] if arg else None
        if arg:
            await all_commands[name].run(msg=message, arg=arg)
        else:
            await all_commands[name].run(msg=message)
