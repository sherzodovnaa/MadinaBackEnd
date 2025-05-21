import sqlalchemy
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import html, Router
from sqlalchemy import insert
from utils.db.db_sqlalch import user, engine
from states.register import Register

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    text = (f"O'zingizga mos til tanlang:\n"
            f"Выберите язык, подходящий для себя:\n"
            f"Choose a language suitable for yourself: \n")

    await message.answer(text)

    chat_id = message.chat.id
    username = message.from_user.username
    fullname = message.from_user.full_name
    try:
        with engine.connect() as conn:
            query = insert(user).values(chat_id=chat_id, fullname=fullname, username=username)
            conn.execute(query)
            conn.commit()
        await state.set_state(Register.lang)
    except sqlalchemy.exc.IntegrityError:
        await message.answer('Siz avval ro`yxatdan o`tib bo`lgansiz!')
        await state.clear()
