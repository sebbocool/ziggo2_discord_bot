import discord

from commands.command import Command
from commands.friend import friend
from commands.mge import mge
from commands.ziggotalk import ziggotalk
from commands.bomba import bomba
from commands.pingziggo import pingziggo
from commands.translate import translate
from commands.extend import extend
from commands.ship import ship
from commands.help_command import help_command

COMMAND_PREFIX = "!"

all_commands: dict[str, Command] = {}


def add_command(cmd: Command, prefix=COMMAND_PREFIX) -> None:
    all_commands[prefix + cmd.get_name()] = cmd


add_command(ziggotalk)
add_command(bomba)
add_command(pingziggo)
add_command(translate)
add_command(extend, "!")
add_command(mge)
add_command(friend)
add_command(ship)
add_command(help_command)


async def run_command(message: discord.Message):
    name, *arg = message.content.strip().split(" ", 1)
    if name in all_commands:
        cmd = all_commands[name]
        arg = arg[0] if arg else None
        await cmd.run(msg=message, arg=arg)
