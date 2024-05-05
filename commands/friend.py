import discord

from commands.command import Command


async def friend(msg: discord.Message, _arg: str | None):
    channel = msg.author.voice.channel

    if channel is None:
        await msg.channel.send("I'm sorry, but I cannot find that voice channel.")
        return

    if msg.channel.guild.voice_client is not None:
        await msg.channel.guild.voice_client.disconnect(force=True)

    await channel.connect()


friend = Command(
    name="friend",
    description="Ask ziggo2 to hangout with you.",
    func=friend
)
