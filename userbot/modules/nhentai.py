# Copyright (C) 2020 KeselekPermen69
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.nhentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@nHentaiBot"
    try:
        await event.edit("```Processing```")
        async with bot.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=424466890)
                )
                await bot.send_message(chat, link)
                response = await response
            except YouBlockedUserError:
                await event.reply(
                    "```Unblock dulu ganteng @nHentaiBot terus coba lagi```"
                )
                return
            if response.text.startswith(
                "**Maaf ganteng gadapet manga yang kamu cari 😭**"
            ):
                await event.edit("```Kira nya Ini bukan link manga```")
            else:
                await event.delete()
                await bot.send_message(event.chat_id, response.message)
    except TimeoutError:
        await event.edit("`Error: ``@nHentaiBot`` Tidak Merespon!`")


CMD_HELP.update(
    {
        "nhentai": ">`.nhentai` <link / kode Nuklir>"
        "\nKegunaan: Lihat di Telegraph mweheheh 😈\n"
    }
)
