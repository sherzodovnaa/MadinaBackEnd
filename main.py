
from aiogram import html, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.button import keyboard
from utlis.static.answers import savol, TELEGRAPH_LINK, quiz
from utlis.static.keyboards import ABOUT_US, ADDRESS, KURS, SAVOL, ADMIN, NUM, LOC

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!", reply_markup=keyboard)




@router.message(Command("quiz"))
async def send_quiz(message: Message):
    await message.answer(text=quiz)
    # await message.answer(text=TELEGRAPH_LINK)






