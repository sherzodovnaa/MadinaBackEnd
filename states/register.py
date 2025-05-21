from aiogram.fsm.state import StatesGroup, State


class FormState(StatesGroup):
    full_name = State()
    phone = State()
    birthday = State()
    address = State()
    email = State()
    passport = State()
