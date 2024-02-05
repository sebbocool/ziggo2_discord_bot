import discord

from commands.command import Command


async def help_command(msg: discord.Message, _):
    from commands import all_commands as cmds
    help_txt = """
               Hello! I'm ziggo2.0, created by ziggo and noot.
                
Commands currently available:
               """
    for name, cmd in cmds.items():
        help_txt += f"""
                      - `{name}{cmd.description}"""

    await msg.channel.send(help_txt)


help_command = Command("help", "`: Shows this message", help_command)
