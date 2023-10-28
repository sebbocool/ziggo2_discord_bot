from ziggo2_discord_bot.commands.ziggotalk import ziggotalk
from ziggo2_discord_bot.commands.bomba import bomba
from ziggo2_discord_bot.commands.pingziggo import pingziggo
from ziggo2_discord_bot.commands.translate import translate
from ziggo2_discord_bot.commands.help_command import help_command

all_commands = {}


def add_command(command) -> None:
    all_commands["/" + command.get_name()] = command


add_command(ziggotalk)
add_command(bomba)
add_command(pingziggo)
add_command(translate)
add_command(help_command)
