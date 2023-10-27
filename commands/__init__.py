from ziggotalk import ziggotalk

commands = {}

def add_command(command) -> None:
    commands[command.get_name()] = command

add_command(ziggotalk)
