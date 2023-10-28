import discord

from ziggo2_discord_bot.commands.command import Command


async def pingziggo(msg: discord.Message, arg: str):
    if msg.channel.name == "bot":
        amount = int(arg)
        if amount != "" and 10 >= int(amount) > 0:
            for i in range(int(amount)):
                await msg.channel.send('<@228889592055463948>')
        else:
            await msg.channel.send('< @228889592055463948>')
    else:
        await msg.channel.send("This command can only be used in #bot", reference=msg)


pingziggo = Command(
    name="pingziggo",
    description=" [1-10]`: Need ziggo's attention? Is he late for the offi? Just wanna disturb? Go wild.",
    func=pingziggo
)
