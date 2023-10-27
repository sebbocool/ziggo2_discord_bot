import deepl
from token_long import DEEPLTOKEN
from command import Command

translator = deepl.Translator(DEEPLTOKEN)
async def translate(msg):
    if msg.content[:3] == "/to" and msg.reference:
        referenced_message = await msg.channel.fetch_message(msg.reference.message_id)
        match msg.content[4:].lower():
            case "se":  # Swedish
                await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="SV"),
                                       reference=msg)
            case "ja":  # Japanese
                await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="JA"),
                                       reference=msg)
            case "de":  # German
                await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="DE"),
                                       reference=msg)
            case "en":  # English
                await msg.channel.send(translator.translate_text(referenced_message.content, target_lang="EN-US"),
                                       reference=msg)
            case other:
                await msg.channel.send("Useless language detected.")

translate = Command("translate", "/to [se/de/en/ja]`: Respond to a message to translate in to the selected target "
                                 "language.", translate)
