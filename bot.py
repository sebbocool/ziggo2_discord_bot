import discord
import random

from commands.ziggotalk import get_ziggo_quote
from config import DISCORD_TOKEN
from commands import run_command, COMMAND_PREFIX


async def add_random_reaction(message: discord.Message):
    beast_emoji = discord.utils.get(message.guild.emojis, name="beast")
    cringe_emoji = discord.utils.get(message.guild.emojis, name="cringe")
    ziggo_emoji = discord.utils.get(message.guild.emojis, name="ziggo")
    emoji_to_use = random.choice([beast_emoji, cringe_emoji, ziggo_emoji])
    if emoji_to_use:
        await message.add_reaction(emoji_to_use)


class Ziggo2(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message: discord.Message):
        if message.author == self.user:
            return

        if "@everyone" in message.content:
            await message.channel.send("https://media.tenor.com/uFeEjGFzmc0AAAAC/stop.gif", reference=message)
            return

        if message.type == discord.MessageType.new_member:
            await message.reply(get_ziggo_quote())

        if random.randint(1, 18) == 6:
            await add_random_reaction(message)

        if message.content.startswith(COMMAND_PREFIX):
            await run_command(message)

    async def on_voice_state_update(
            self,
            member: discord.Member,
            _before: discord.VoiceState,
            _after: discord.VoiceState
    ):
        voice = discord.utils.get(self.voice_clients, guild=member.guild)

        if voice is None:
            return

        channel = voice.channel

        if isinstance(channel, discord.VoiceChannel) and len(channel.members) == 1:
            await voice.disconnect(force=False)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Ziggo2(intents=intents)
client.run(DISCORD_TOKEN)
