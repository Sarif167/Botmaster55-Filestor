
from pyrogram.errors import UserNotParticipant
from info import FSUB_CHANNEL_1, FSUB_CHANNEL_2

async def check_fsub(bot, user_id):
    try:
        await bot.get_chat_member(FSUB_CHANNEL_1, user_id)
        await bot.get_chat_member(FSUB_CHANNEL_2, user_id)
        return True
    except UserNotParticipant:
        return False

async def send_fsub_message(message):
    btn = [[
        ("Join Channel 1", f"https://t.me/c/{str(FSUB_CHANNEL_1)[4:]}"),
        ("Join Channel 2", f"https://t.me/c/{str(FSUB_CHANNEL_2)[4:]}")
    ]]
    await message.reply_text(
        "⚠️ Please join both channels to use this bot!",
    )
