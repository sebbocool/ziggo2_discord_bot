import discord

from commands.command import Command


async def help_command(msg: discord.Message, _):
    from commands import all_commands as cmds
    help_txt = """
               Hello! I'm ziggo2.0, created by ziggo and noot.
                
Commands currently available:
               """

    for name, cmd in cmds.items():
        arg_info = cmd.get_arg_info()
        if arg_info is None:
            help_txt += f"\n- `{name}`: {cmd.get_description()}"
        else:
            help_txt += f"\n- `{name} [{arg_info}]`: {cmd.get_description()}"

    await msg.channel.send(help_txt)


help_command = Command(
    name="help",
    description="Show this message.",
    func=help_command
)
