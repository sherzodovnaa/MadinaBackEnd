from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from utlis.static.answers import quiz, TELEGRAPH_LINK

filter_router = Router()

@filter_router.message(Command("quiz"))
async def send_quiz(message: Message):
    await message.answer(text=quiz)
    await message.answer(text=TELEGRAPH_LINK)