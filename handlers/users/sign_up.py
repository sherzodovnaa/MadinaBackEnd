from multiprocessing.resource_tracker import register
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register import FormState

register_router = Router()

@register_router.message(Command("register"))
async def register_start(message: Message, state: FSMContext ):
    await message.answer("Ism familiya kiriting")
    await state.set_state(FormState.full_name)

@register_router.message(FormState.full_name)
async def get_fullname(message: Message, state: FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Telefon raqamingizni kiriting")
    await state.set_state(FormState.phone)

@register_router.message(FormState.phone)
async def get_phone_number(message: Message, state: FSMContext):
    phone=message.text
    await state.update_data(phone=phone)
    await message.answer("Tug'ilgan kuningizni kiriting: dd.mm.yy")
    await state.set_state(FormState.birthday)


@register_router.message(FormState.birthday)
async def get_birthday(message: Message, state: FSMContext):
    birthday=message.text
    await state.update_data(birthday=birthday)
    await message.answer("Manzilingizni kiriting")
    await state.set_state(FormState.address)



@register_router.message(FormState.address)
async def get_address(message: Message, state: FSMContext):
    address=message.text
    await state.update_data(address=address)
    await message.answer("Emailingizni kiriting")
    await state.set_state(FormState.email)


@register_router.message(FormState.email)
async def get_email(message: Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)  # save to state
    await message.answer("Pasportingiz seriyasini kiriting ")
    await state.set_state(FormState.passport)


@register_router.message(FormState.passport)
async def get_passport(message: Message, state: FSMContext):
    passport = message.text
    await state.update_data(passport=passport)  # save to state

    datas = await state.get_data()
    full_name = datas.get("full_name")
    phone = datas.get("phon")
    birthday = datas.get("birhtday")
    address = datas.get("address")
    email = datas.get("email")
    passport = datas.get("pasport")

    await message.answer("Ro'yhadan muvaffaqiyatli o'tdi")
    await message.answer("Register natijasi: \n"
                         f"1.Full_name: {full_name}\n"
                         f"2.Phone: {phone}\n"
                         f"3.Birthday:{birthday}\n"
                         f"4.Address: {address}\n"
                         f"5.Email: {email}\n"
                         f"6.Passport seriya: {passport}")
    await state.clear()