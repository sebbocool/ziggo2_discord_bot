import discord

from commands.command import Command

ZIGGO_MENTION = '<@228889592055463948>'


async def pingziggo(msg: discord.Message, arg: str | None):
    if msg.channel.name != "bot":
        await msg.channel.send("This command can only be used in #bot", reference=msg)
        return

    amount = int(arg)
    if amount == "" or (10 < int(amount) or int(amount) <= 0):
        await msg.channel.send(ZIGGO_MENTION)
        return

    for i in range(int(amount)):
        await msg.channel.send(ZIGGO_MENTION)


pingziggo = Command(
    name="pingziggo",
    description=" [1-10]`: Need ziggo's attention? Is he late for the offi? Just wanna disturb? Go wild.",
    func=pingziggo
)
