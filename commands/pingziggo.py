import discord

from commands.command import Command
from common.parsing import to_int

ZIGGO_MENTION = '<@228889592055463948>'
MIN_AMOUNT = 1
MAX_AMOUNT = 10


async def send_ping_messages(msg: discord.Message, amount: int) -> None:
    for i in range(int(amount)):
        await msg.channel.send(ZIGGO_MENTION)


async def pingziggo(msg: discord.Message, arg: str | None):
    if msg.channel.name != "bot":
        await msg.channel.send("This command can only be used in #bot", reference=msg)
        return

    amount = to_int(arg, MIN_AMOUNT)

    if amount > MAX_AMOUNT:
        await msg.channel.send("It's too much >.<")
        await send_ping_messages(msg, MAX_AMOUNT)
    elif amount < MIN_AMOUNT:
        await msg.channel.send("Baka")
    else:
        await send_ping_messages(msg, amount)


pingziggo = Command(
    name="pingziggo",
    arg=f"{MIN_AMOUNT}-{MAX_AMOUNT}",
    description="Need ziggo's attention? Is he late for the offi? Just wanna disturb? Go wild.",
    func=pingziggo
)
