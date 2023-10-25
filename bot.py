from token_long import TOKEN, DEEPLTOKEN
import discord
import deepl
import asyncio
import random

translator = deepl.Translator(DEEPLTOKEN)

def get_ziggo_quote():
    with open("ziggoquotes.txt", "r") as file:
        quotes = file.readlines()
        quote = "ziggokill: " + random.choice(quotes).strip()
    return quote


class ziggo2(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    ### COMMANDS ###
    async def translate(self, msg):
        if msg.content[:3] == "/to" and msg.reference:
            referenced_message = await msg.channel.fetch_message(msg.reference.message_id)
            match msg.content[4:].lower():
                case "se":  # Swedish
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="SV"), reference=msg)
                case "ja":  # Japanese
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="JA"), reference=msg)
                case "de":  # German
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="DE"), reference=msg)
                case "en":  # English
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="EN-US"), reference=msg)
                case other:
                    await msg.channel.send("Useless language detected.")

    async def pingziggo(self, msg):
        amount = msg.content[11:]
        if amount != "" and 10 >= int(amount) > 0:
            for i in range(int(amount)):
                await msg.channel.send('<@228889592055463948>')
        else:
            await msg.channel.send('<@228889592055463948>')

    async def ziggo_quote(self, msg):
        quote = get_ziggo_quote()
        await msg.channel.send(quote, reference=msg)

    async def bomba(self, msg):
        target = msg.content[7:]
        if len(target) == 0:
            target = "the Medic"

        author = msg.author.mention

        await msg.channel.send(f"{author} bombs {target}, and...")
        await asyncio.sleep(1)

        choices = [
            (10, f"{author} beefs."),
            (10, f"{author} fails his jump..."),
            (9, f"{author} misses his rockets..."),
            (9, f"{author} gets denied."),
            (8, f"{author} craters."),
            (8, f"{author} dies to a trap."),
            (8, f"{target} surfs away."),
            (7, f"{author} gets airshot!"),
            (7, f"{author} forces {target}!"),
            (7, f"{author} dies, but forces {target} nonetheless!"),
            (6, f"{author} gets airpiped!"),
            (6, f"{author} dominates {target}!"),
            (6, f"{target} pulls off a clutch save with the ÜberSaw!"),
            (6, f"{author} forces {target}, and gets out!"),
            (6, f"{author} misses, but {target} uses anyway!"),
            (5, f"{author} kills {target}! Looks like someone forgot to build."),
            (5, f"{target} hits a crossbow airshot!"),
            (5, f"{author} kills {target}! He was on Kritzkrieg all along!"),
            (5, f"{author} syncs his rockets! It's a force!"),
            (5, f"{author} misses {target}, but kills a Soldier instead!"),
            (5, f"{author} misses {target}, but kills a Scout instead!"),
            (4, f"{author} misses {target}, but kills the Demo instead!"),
            (4, f"{author} gets headshot mid air!"),
            (4, f"{author} airshots {target}! It's a force!"),
            (4, f"{target} lives on 1 HP."),
            (4, f"{target} gets forced by the team's spam."),
            (3, f"{author} is out of ammo?"),
            (3, f"{author} drops {target}!"),
            (3, f"{target} was hiding in the forward spawn..."),
            (3, f"{author} syncs his rockets! It's a drop!"),
            (2, f"{author} lost connection to the server!"),
            (2, f"{author} timed out."),
            (2, f"{author} airshots {target}! It's a drop!"),
            (2, f"{author} drops {target}, and kills them all!"),
            (1, f"{author} disconnected. (VAC banned from secured server)"),
        ]

        weights, population = zip(*choices)

        result = random.choices(population, weights)[0]

        await msg.channel.send(result)

    ### READ MESSAGES ###
    async def on_message(self, message):
        if message.author == self.user:
            return

        if "@everyone" in message.content:
            await message.channel.fetch_message(message.id)
            await message.channel.send("https://media.tenor.com/uFeEjGFzmc0AAAAC/stop.gif", reference=message)
            return

        if random.randint(1, 12) == 6:
            beast_emoji = discord.utils.get(message.guild.emojis, name="beast")
            cringe_emoji = discord.utils.get(message.guild.emojis, name="cringe")
            ziggo_emoji = discord.utils.get(message.guild.emojis, name="ziggo")

            emoji_to_use = random.choice([beast_emoji, cringe_emoji, ziggo_emoji])
            if emoji_to_use:
                await message.add_reaction(emoji_to_use)

        if message.content.startswith("/pingziggo") and message.channel.name == "bot":
            await self.pingziggo(message)

        elif message.content.startswith("/to"):
            await self.translate(message)

        elif message.content.startswith("/ziggotalk"):
            await self.ziggo_quote(message)

        elif message.content.startswith("/bomba"):
            await self.bomba(message)

        elif message.type == discord.MessageType.new_member:
            reply = get_ziggo_quote()
            await message.reply(reply)

        elif message.content.startswith("/help"):
            help = """
            Hello! I'm ziggo2.0, created by ziggo and noot. 
                   
    Commands currently available:                    
                    - `/pingziggo [1-10]`: Need ziggo's attention? Is he late for the offi? Just wanna disturb? Go wild.
                    - `/to [se/de/en/ja]`: Respond to a message to translate in to the selected target language.
                    - `/ziggotalk`: Need some motivation? Get a real quote from one of ziggo's logs.
                    - `/bomba [target]`: Simulate a bomb, will you drop the medic or feed embarrassingly?"""
            await message.channel.send(help)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = ziggo2(intents=intents)
client.run(TOKEN)
