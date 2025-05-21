from logging.handlers import RotatingFileHandler

from aiogram.types import Message
from aiogram import F, Router

from main import router
from utlis.static.answers import quiz
from utlis.static.keyboards import ADMIN

callback_router = Router()


@callback_router.message(F.text == ADMIN)
async def get_Admin_contact_handler(message: Message):
    number = "+998950032737"
    await message.answer_contact(phone_number=number, first_name="👮🏻 Admin", last_name="Madina")


@callback_router.message(F.contact)
async def get_contact_handler(message: Message):
    if message.contact:
        phone_number = message.contact.phone_number
        await message.answer(f"Telefon raqamingiz: {phone_number} qabul qilindi!")
    else:
        await message.answer("Telefon raqam yuborilmadi. Iltimos, qayta urinib ko'ring.")
