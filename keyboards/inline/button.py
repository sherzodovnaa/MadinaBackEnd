from mailbox import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pip._internal.cli.base_command import Command

from main import router
from utlis.static.answers import quiz

keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="https://t.me/ziyo_maskani"),
            InlineKeyboardButton(text="Instagram", url="https://instagram.com/madi._na0826"),
        ]
    ])


@router.message(Command("quiz"))
async def send_quiz(message: Message):
    await message.answer(text=quiz)
    # await message.answer(text=TELEGRAPH_LINK)
