from token_long import TOKEN, DEEPLTOKEN
import discord
import deepl
import random
import asyncio

translator = deepl.Translator(DEEPLTOKEN)

class ziggo2(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    ### COMMANDS ###
    async def translate(self, msg):
        if msg.content[:3] == "/to" and msg.reference:
            referenced_message = await msg.channel.fetch_message(msg.reference.message_id)
            match msg.content[4:].lower():
                case "se":  # Swedish
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="SV"))
                case "ja":  # Japanese
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="JA"))
                case "de":  # German
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="DE"))
                case "en":  # English
                    await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="EN"))
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
        with open("ziggoquotes.txt", "r") as file:
            quotes = file.readlines()
            quote = "ziggokill: " + random.choice(quotes).strip()
        await msg.channel.send(quote)

    async def bomba(self, msg):
        target = msg.content[7:]
        if len(target) == 0:
            target = "the Medic"

        author = msg.author.mention

        await msg.channel.send(f"{author} bombs {target}, and...")

        await asyncio.sleep(1)

        result = random.choices([
            f"{author} beefed.",
            f"{author} forced {target}!",
            f"{author} dropped {target}!",
            f"{author} killed them all!"
        ], [50, 30, 15, 5])[0]

        await msg.channel.send(result)


    ### READ MESSAGES ###



    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("/pingziggo"):
            await self.pingziggo(message)

        elif message.content.startswith("/to"):
            await self.translate(message)

        elif message.content.startswith("/ziggotalk"):
            await self.ziggo_quote(message)

        elif message.content.startswith("/bomba"):
            await self.bomba(message)

        elif message.content.startswith("/help"):
            pass


intents = discord.Intents.default()
intents.message_content = True

client = ziggo2(intents=intents)
client.run(TOKEN)
