import discord
from commands.command import Command
import asyncio

import random

shipping_messages = {
    10: [
        ":nauseated_face: Absolutely not... Please stay as far away as possible. :nauseated_face:",
        ":no_entry_sign: This match was a mistake, maybe even a crime. :no_entry_sign:",
        ":x: Just no. The stars are not aligned for you two... :x:",
    ],
    20: [
        ":thinking: Are you sure about this? This seems... awkward. :thinking:",
        ":sweat_smile: It’s a very low chance, but miracles do happen. :sweat_smile:",
        ":face_with_raised_eyebrow: Hmm... maybe try being just friends? :face_with_raised_eyebrow:",
    ],
    30: [
        ":confused: Not looking great, but maybe there's a spark somewhere? :confused:",
        ":neutral_face: Well, it's not the worst... but also not great. :neutral_face:",
        ":grimacing: Yikes... might want to think this one over. :grimacing:",
    ],
    40: [
        ":pensive: It's possible, but it’ll take some work. :pensive:",
        ":shrug: Meh, there might be something there, but it’s weak. :shrug:",
        ":face_with_monocle: Hmm, this could go either way. :face_with_monocle:",
    ],
    50: [
        ":thinking: Right in the middle! Not bad, not great. :thinking:",
        ":relieved: There's a chance, but it's going to need effort! :relieved:",
        ":face_with_raised_eyebrow: It could work, with a bit of luck. :face_with_raised_eyebrow:",
    ],
    60: [
        ":smirk: There's potential here! Keep it up! :smirk:",
        ":ok_hand: Hey, this could actually go somewhere! :ok_hand:",
        ":blush: Not bad at all. There's something here. :blush:",
    ],
    70: [
        ":smiling_face_with_3_hearts: Things are heating up! There’s real potential! :smiling_face_with_3_hearts:",
        ":thumbsup: I see good vibes here! Go for it! :thumbsup:",
        ":wink: Nice match! You two could make this work. :wink:",
    ],
    80: [
        ":heart: This couple is looking really solid! :heart:",
        ":sparkles: You two are almost perfect together! :sparkles:",
        ":star2: This could be something special! Keep going! :star2:",
    ],
    90: [
        ":two_hearts: Love is in the air! This could be the real deal. :two_hearts:",
        ":heart_eyes: Wow, you two are amazing together! :heart_eyes:",
        ":star-struck: You two were practically made for each other! :star-struck:",
    ],
    100: [
        ":heartpulse: This is true love! Perfect match! :heartpulse:",
        ":sparkling_heart: You two are soulmates. Don’t ever let go! :sparkling_heart:",
        ":heart: THIS COUPLE IS PERFECT!! :heart:",
    ]
}

def get_shipping_message(score):
    for index in range(10,110,10):
        if score <= index:
            return random.choice(shipping_messages[index])
    return ":grey_question: Unable to determine compatibility... :grey_question:"


def calculate_compatibility(id1: int, id2: int) -> int:
    return (id1 ^ id2) % 101


def extract_name(user: discord.User | discord.Member) -> str:
    if user.nick is not None:
        return user.nick

    if user.global_name is not None:
        return user.global_name

    if user.name is not None:
        return user.name

    return str(user)


def generate_ship_name(name1: str, name2: str) -> str:
    if len(name1) > 100:
        return "Steve"
    if len(name2) > 100:
        return "Alex"

    name1 = name1.lower()
    name2 = name2.lower()

    for index, letter in enumerate(name1):
        for index2, letter2 in enumerate(name2):
            if letter == letter2:
                shipname = name1[:index] + name2[index2:]
                if (
                    len(shipname) > 3
                    and shipname != name1
                    and shipname != name2
                    and shipname not in name1
                    and shipname not in name2
                ):
                    return shipname.title()

    name1_index = int(round(len(name1) * 0.6))
    name2_index = int(round(len(name2) * 0.4))
    shipname = name1[:name1_index] + name2[name2_index:]
    return shipname.title()


async def ship(msg: discord.Message, arg: str | None):

    users = msg.mentions

    if len(users) == 0:
        await msg.channel.send("Who should we ship?? :smiling_imp:")
        return

    if len(users) > 2:
        await msg.channel.send("No polyamory")
        return

    if len(users) == 1:
        name2 = extract_name(msg.author)
        id2 = msg.author.id
    else:
        name2 = extract_name(users[1])
        id2 = users[1].id

    name1 = extract_name(users[0])
    id1 = users[0].id

    shipname = generate_ship_name(name1, name2)

    compatibility = calculate_compatibility(id1, id2)

    await msg.channel.send(f":revolving_hearts: Shipping <@{id1}> and <@{id2}> !! :revolving_hearts:")
    await asyncio.sleep(1)
    await msg.channel.send(f":sparkles: Their ship name is **{shipname.upper()}**")
    await asyncio.sleep(1)
    await msg.channel.send(f":chart_with_upwards_trend: Their compatibility is **{compatibility}%**")
    await asyncio.sleep(1)
    await msg.channel.send(get_shipping_message(compatibility))


ship = Command(name="ship", arg="people to ship", description="Ship two people.", func=ship)
