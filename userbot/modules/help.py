# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot help command"""

import asyncio

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.help(?: |$)(.*)")
async def help(event):
    """For .help command."""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            msg = await event.edit(str(CMD_HELP[args]))
        else:
            msg = await event.edit("Yang Bener Ganteng.")
    else:
        head = "Yang Bener Ganteng Ngetik Command nya !!"
        head2 = f"Module Ganteng yang Di Load : {len(CMD_HELP)}"
        head3 = "Gunakan: `.help` `<nama module>`"
        head4 = "List Command Dengan Kegantengan di Bawah: "
        string = ""
        sep1 = "`••••••••••••••••••••••••••••••••••••••••••••••`"
        sep2 = "`=========================================`"
        for i in sorted(CMD_HELP):
            string += "`" + str(i)
            string += "`  ⚡  "
        await event.edit(
            f"{head}\
              \n{head2}\
              \n{head3}\
              \n{sep2}\
              \n{head4}\
              \n\n{string}\
              \n{sep1}"
        )
    await asyncio.sleep(40)
    await event.delete()
    try:
        await msg.delete()
    except BaseException:
        return  # just in case if msg deleted first
