from commands.ziggotalk import ziggotalk
from commands.bomba import bomba
from commands.pingziggo import pingziggo
from commands.translate import translate
from commands.help_command import help_command

all_commands = {}


def add_command(command) -> None:
    all_commands["/" + command.get_name()] = command


add_command(ziggotalk)
add_command(bomba)
add_command(pingziggo)
add_command(translate)
add_command(help_command)

if __name__ == '__main__':
    print(all_commands.keys())
