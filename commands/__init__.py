import discord

from ziggo2_discord_bot.commands.ziggotalk import ziggotalk
from ziggo2_discord_bot.commands.bomba import bomba
from ziggo2_discord_bot.commands.pingziggo import pingziggo
from ziggo2_discord_bot.commands.translate import translate
from ziggo2_discord_bot.commands.help_command import help_command

COMMAND_PREFIX = "/"

all_commands = {}


def add_command(command) -> None:
    all_commands[COMMAND_PREFIX + command.get_name()] = command


add_command(ziggotalk)
add_command(bomba)
add_command(pingziggo)
add_command(translate)
add_command(help_command)


async def run_command(message: discord.Message):
    name, *arg = message.content.strip().split(" ", len(COMMAND_PREFIX))
    if name in all_commands:
        arg = arg[0] if arg else None
        if arg:
            await all_commands[name].run(msg=message, arg=arg)
        else:
            await all_commands[name].run(msg=message)
