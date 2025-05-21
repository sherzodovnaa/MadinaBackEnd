from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy import insert, select, update
from utils.db.db_sqlalch import user, engine

from states.register import Register

register_router = Router()


@register_router.message(Register.lang)
async def save_lang(message: Message, state: FSMContext):
    til = message.text
    chat_id = message.chat.id

    with engine.connect() as conn:
        query = update(user).where(user.c.chat_id == chat_id).values(lang=til)
        conn.execute(query)
        conn.commit()

    await state.set_state(Register.fullname)
    await message.answer("Til qo'shildi")
    await message.answer("To'liq ismingiz kiriting: ")


@register_router.message(Register.fullname)
async def save_fullname(message: Message, state: FSMContext):
    fullname = message.text
    chat_id = message.chat.id

    with engine.connect() as conn:
        query = update(user).where(user.c.chat_id == chat_id).values(fullname=fullname)
        conn.execute(query)
        conn.commit()

    await state.set_state(Register.phone)
    await message.answer("Ism qo'shildi")
    await message.answer("Telefon raqamingizni kiriting: ")


@register_router.message(Register.phone)
async def save_fullname(message: Message, state: FSMContext):
    phone = message.text
    chat_id = message.chat.id

    with engine.connect() as conn:
        query = update(user).where(user.c.chat_id == chat_id).values(phone=phone)
        conn.execute(query)
        conn.commit()

    await state.set_state(Register.fullname)
    await message.answer("Telfon raqam qo'shildi")
    await state.clear()
