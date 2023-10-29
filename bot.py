import discord
import random

from ziggo2_discord_bot.token_long import TOKEN
from ziggo2_discord_bot.commands import run_command, COMMAND_PREFIX


async def add_random_reaction(message):
    beast_emoji = discord.utils.get(message.guild.emojis, name="beast")
    cringe_emoji = discord.utils.get(message.guild.emojis, name="cringe")
    ziggo_emoji = discord.utils.get(message.guild.emojis, name="ziggo")
    emoji_to_use = random.choice([beast_emoji, cringe_emoji, ziggo_emoji])
    if emoji_to_use:
        await message.add_reaction(emoji_to_use)


class ziggo2(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "@everyone" in message.content:
            await message.channel.fetch_message(message.id)
            await message.channel.send("https://media.tenor.com/uFeEjGFzmc0AAAAC/stop.gif", reference=message)
            return

        if random.randint(1, 12) == 6:
            await add_random_reaction(message)

        if message.content.startswith(COMMAND_PREFIX):
            await run_command(message)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = ziggo2(intents=intents)
client.run(TOKEN)
