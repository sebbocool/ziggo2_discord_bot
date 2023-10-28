import discord
import random

from ziggo2_discord_bot.token_long import TOKEN
from ziggo2_discord_bot.commands import all_commands as cmds


class ziggo2(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    ### READ MESSAGES ###
    async def on_message(self, message):
        if message.author == self.user:
            return

        if "@everyone" in message.content:
            await message.channel.fetch_message(message.id)
            await message.channel.send("https://media.tenor.com/uFeEjGFzmc0AAAAC/stop.gif", reference=message)
            return

        ### sometimes react with a random emoji
        if random.randint(1, 12) == 6:
            beast_emoji = discord.utils.get(message.guild.emojis, name="beast")
            cringe_emoji = discord.utils.get(message.guild.emojis, name="cringe")
            ziggo_emoji = discord.utils.get(message.guild.emojis, name="ziggo")

            emoji_to_use = random.choice([beast_emoji, cringe_emoji, ziggo_emoji])
            if emoji_to_use:
                await message.add_reaction(emoji_to_use)

        ### check if message is a command
        if message.content.startswith("/"):
            name, *arg = message.content.strip().split(" ", 1)
            if name in cmds:
                arg = arg[0] if arg else None
                if arg:
                    await cmds[name].run(msg=message, arg=arg)
                else:
                    await cmds[name].run(msg=message)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = ziggo2(intents=intents)
client.run(TOKEN)
