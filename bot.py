from token_long import TOKEN, DEEPLTOKEN
import discord
import deepl

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
                case other:
                    await msg.channel.send("Useless language detected.")

    async def pingziggo(self, msg):
        amount = msg.content[11:]
        if amount != "" and 10 >= int(amount) > 0:
            for i in range(int(amount)):
                await msg.channel.send('<@228889592055463948>')
        else:
            await msg.channel.send('<@228889592055463948>')

    ### READ MESSAGES ###
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content[:10] == "/pingziggo":
            await self.pingziggo(message)

        if message.content[:3] == "/to":
            await self.translate(message)


intents = discord.Intents.default()
intents.message_content = True

client = ziggo2(intents=intents)
client.run(TOKEN)
