"""

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, LOGGER_ID
from JioSavaan import iapp
from JioSavaan.core.userbot import assistants
from JioSavaan.utils.assistant import get_assistant_details
from JioSavaan.utils.assistant import is_avl_assistant as assistant
from JioSavaan.utils.database import get_assistant, save_assistant, set_assistant
from JioSavaan.utils.decorators import AdminActual


@iapp.on_message(filters.command("changeassistant") & ~BANNED_USERS)
@AdminActual
async def assis_change(client, message: Message, _):
    if await assistant() == True:
        return await message.reply_text(
            "sᴏʀʀʏ sɪʀ! ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ ᴏɴʟʏ ᴏɴʀ ᴀssɪsᴛᴀɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʜᴇʀᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴᴛ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ"
        )
    usage = f"**ᴅᴇᴛᴇᴄᴛᴇᴅ ᴡʀᴏɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴜsᴀsɢᴇ \n**ᴜsᴀsɢᴇ:**\n/changeassistant - ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ's ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʀᴀɴᴅᴏᴍ ᴀssɪsᴛᴀɴᴛ ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ"
    if len(message.command) > 2:
        return await message.reply_text(usage)
    a = await get_assistant(message.chat.id)
    DETAILS = f"ʏᴏᴜʀ ᴄʜᴀᴛ's ᴀssɪsᴛᴀɴᴛ ʜᴀs ʙᴇᴇɴ ᴄʜᴀɴɢᴇᴅ ғʀᴏᴍ [{a.fristname}](https://t.me/{a.username}) "
    if not message.chat.id == LOGGER_ID:
        try:
            await a.leave_chat(message.chat.id)
        except:
            pass
    b = await set_assistant(message.chat.id)
    DETAILS += f"ᴛᴏ [{b.name}](https://t.me/{b.username})"
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(DETAILS, disable_web_page_preview=True)


@iapp.on_message(filters.command("setassistant") & ~BANNED_USERS)
@AdminActual
async def assis_set(client, message: Message, _):
    if await assistant():
        return await message.reply_text(
            "sᴏʀʀʏ sɪʀ! ɪɴ ʙᴏᴛ sᴇʀᴠᴇʀ ᴏɴʟʏ ᴏɴᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴠᴀɪʟᴀʙʟᴇ ᴛʜᴇʀᴇғᴏʀᴇ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴄʜᴀɴɢᴇ ᴀssɪsᴛᴀɴᴛ"
        )
    usage = await get_assistant_details()
    if len(message.command) != 2:
        return await message.reply_text(usage, disable_web_page_preview=True)
    query = message.text.split(None, 1)[1].strip()
    if query not in assistants:
        return await message.reply_text(usage, disable_web_page_preview=True)
    a = await get_assistant(message.chat.id)
    try:
        await a.leave_chat(message.chat.id)
    except:
        pass
    await save_assistant(message.chat.id, query)
    b = await get_assistant(message.chat.id)
    try:
        await b.join_chat(message.chat.id)
    except:
        pass
    await message.reply_text(
        "**Yᴏᴜʀ ᴄʜᴀᴛ's ɴᴇᴡ ᴀssɪsᴛᴀɴᴛ ᴅᴇᴛᴀɪʟs:**\nAssɪsᴛᴀɴᴛ Nᴀᴍᴇ :- {b.fristname}\nUsᴇʀɴᴀᴍᴇ :- @{b.username}\nID:- {b.id}",
        disable_web_page_preview=True,
    )


@iapp.on_message(filters.command("checkassistant") & filters.group & ~BANNED_USERS)
@AdminActual
async def check_ass(client, message: Message, _):
    a = await get_assistant(message.chat.id)
    await message.reply_text(
        "**Yᴏᴜʀ ᴄʜᴀᴛ's ᴀssɪsᴛᴀɴᴛ ᴅᴇᴛᴀɪʟs:**\nAssɪsᴛᴀɴᴛ Nᴀᴍᴇ :- {a.fristname}\nAssɪsᴛᴀɴᴛ\nUsᴇʀɴᴀᴍᴇ :- @{a.username}\nAssɪsᴛᴀɴᴛ ID:- {a.id}",
        disable_web_page_preview=True,
    )

"""