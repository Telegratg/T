# ๐๐๐๐๐๐ค๐ฃ ยฎ
# ุงููููู ุญูููู ููุชุงุจูุฉ ุฒููุฒุงู ุงูููุจูู โคถ @zzzzl1l ุฎุงุต ุจุณููุฑุณ โคถ ๐๐๐๐๐๐ค๐ฃ


import random

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import (
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    InputMessagesFilterVoice,
)

from zthon import zedub

from ..core.managers import edit_or_reply
from . import reply_id


@zedub.zed_cmd(pattern="ุญุงูุงุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event, "**โฎ . ุงูุซูุฑ ููู 500 ุญูุงูุงุช ูุงุชูุณ ูุตููุฑุฉ .. ุงุฑุณูู .ุญุงูุงุช ูุงุชุณ ๐ซโฐ**"
        )
    chat = "@amaterody_bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุญูุงูุงุช ูุงุชูุณ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1569771593)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @amaterody_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุณุชูุฑู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุณุชููุฑูุงุช ุงูููู ูุตููุฑุฉ ููุทูุฑูููู.. ุงุฑุณูู .ุณุชูุฑู ุงููู ๐ซโฐ**",
        )
    chat = "@Chhhbbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุณูุชูุฑู ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1915672327)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Chhhbbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุฑูุงุฏู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โโุงูุชูุงุฑุงุช ูููุฏ ุฑููุงุฏููู ๐๐ปโโ๐**\n**โโููู ุจุงุถุงููุฉ ุฑููู? ูู 130 - 1 ููุงููุฑ . . ูุซูุงู ( .ุฑูุงุฏู 1 ) ...๐ซโฐ**",
        )
    chat = "@QQY_98BOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2088144968)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @QQY_98BOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุฑููู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โโููุงุทูุน ุฑูููู ุดุฑุนููุฉ ๐๐ธ**\n**โโููู ุจุงุถุงููุฉ ุฑููู? ูู 200 - 1 ููุงููุฑ . . ูุซูุงู ( .ุฑููู 1 ) ...๐ซโฐ**",
        )
    chat = "@ZlZZl77bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูููู ุงูุดูุฑุนูู ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1956894280)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZlZZl77bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุฑูุงุฏูู ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โโุงูุชูุงุฑุงุช ุจููุงุช ุฑููุงุฏููู ๐๐ปโโ๐**\n**โโููู ุจุงุถุงููุฉ ุฑููู? ูู 130 - 1 ููุงููุฑ . . ูุซูุงู ( .ุฑูุงุฏูู 1 ) ...๐ซโฐ**",
        )
    chat = "@SSSS_sssiBOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2076530727)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @SSSS_sssiBOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุจูุณุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โโุงูุชูุงุฑุงุช ุจูุณุช ุชุทูููู ุจููุงุช ๐ฏโโ๐**\n**โโููู ุจุงุถุงููุฉ ุฑููู? ูู 29 - 1 ููุงููุฑ . . ูุซูุงู ( .ุจูุณุช 1 ) ...๐ซโฐ**",
        )
    chat = "@Zedthonbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุขูุชูุงุฑ ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1863051724)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Zedthonbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุญุจ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โโุงูุชูุงุฑุงุช ุชุทูููู ุญุจ โฅ๏ธ๐**\n**โโููู ุจุงุถุงููุฉ ุฑููู? ูู 57 - 1 ููุงููุฑ . . ูุซูุงู ( .ุญุจ 1 ) ...๐ซโฐ**",
        )
    chat = "@ZlZZl777BOT"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุขูุชูุงุฑ ... ๐งธ๐**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=2099294312)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZlZZl777BOT .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุฑูุงูุดู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูุงูุดูู ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** ๐ฌโุฑูุงูุดูู ุชุญุดููุด โง๐๐นโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุงุฏุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ููุทูุน ุงุฏุช ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**๐ฌโููุงุทูุน ุงููุฏุช ูููุนูู โง ๐ค๐ญโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุบูููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูููุทูุน ...**")
    try:
        zedgan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชูุงเขช ุงูุงุบูููู ูู ๐๐ถ**ูดโ โ โ โ โ โ โ โ โ โ โ โย?โ โ\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุดุนุฑ$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุดุนูุฑ ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชููุงุฑ ููุทูุน ุงูุดุนูุฑ ููุฐุง ูู**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ูููุฒ$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูููููุฒ ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**โฆโุชู ุงุฎุชููุงุฑ ููุทูุน ุงูููููุฒ ููุฐุง ูู**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฑู ุงูุดู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุฑูุงูุดูู ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**๐โุฑูุงูุดูู ุชุญุดููุด โง๐๐นโ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ูุนูููู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุตููุฑุฉ ููุนููููุฉ ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**๐โุตููุฑุฉ ููุนููููุฉ โง ๐ค๐กโ**\n\n[โง??๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุชููุช$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ููุช ุชูููุช ุจุงูุตููุฑ ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**โฆโููุช ุชูููุช ุจุงูุตููุฑ โงโ๏ธ๐โ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ุฎูุฑูู$")
async def _(event):
    zzevent = await edit_or_reply(event, "**โฎโขโ ููู ุฎููุฑูู ุจุงูุตููุฑ ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**โฆโููู ุฎููุฑูู  โงโ๏ธ๐โ**\n\n[โง๐๐ค๐ช๐ง๐๐ ๐๐๐๐๐๐ค๐ฃ](https://t.me/ZedThon)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")


@zedub.zed_cmd(pattern="ููุฏ ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุดุจูุงุจ ููุทูุฑูููู.. ุงุฑุณูู .ููุฏ ุงููู ๐ซโฐ**",
        )
    chat = "@ZelTrbot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1354728480)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @ZelTrbot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)


@zedub.zed_cmd(pattern="ุจูุช ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id and not event.pattern_match.group(1):
        reply_to_id = await event.get_reply_message()
        reply_to_id = str(reply_to_id.message)
    else:
        reply_to_id = str(event.pattern_match.group(1))
    if not reply_to_id:
        return await edit_or_reply(
            event,
            "**โฎ . ุงูุซูุฑ ููู 1000 ุงูุชูุงุฑุงุช ุงูููู ุจููุงุช ููุทูุฑูููู.. ุงุฑุณูู ..ุจูุช ุงููู ๐ซโฐ**",
        )
    chat = "@Maroooosh_bot"
    zzevent = await edit_or_reply(event, "**โฎโขโ ุฌูุงุฑู ุชุญูููู ุงูุงูุชูุงุฑ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1000915223)
            )
            await event.client.send_message(chat, "{}".format(input_str))
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await zzevent.edit(
                "**โฎโขโ ุชุญููู ูู ุงููู ูู ุชููู ุจุญุธุฑ ุงูุจูุช @Maroooosh_bot .. ุซู ุงุนูุฏ ุงุณุชุฎุฏุงู ุงูุงููุฑ ...๐คโฅ๏ธ**"
            )
            return
        if response.text.startswith("I can't find that"):
            await zzevent.edit("**โฎโขโ ุนูุฐุฑุงู .. ููู ุงุณุชุทูุน ุงูุฌูุงุฏ ุงููุทูููุจ โน๏ธ๐**")
        else:
            await zzevent.delete()
            await event.client.send_message(event.chat_id, response.message)
