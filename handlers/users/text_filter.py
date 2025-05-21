from aiogram.types import Message
from aiogram import F, Router
from keyboards.default.button import keyboard
from main import router
from utlis.static.answers import savol, TELEGRAPH_LINK
from utlis.static.keyboards import ABOUT_US, ADDRESS, KURS, SAVOL


@router.message(F.text == ABOUT_US)
async def about_us(message: Message):
    biz =  "AgACAgIAAxkBAWw5EGf5NJfLo8gOW2pQgCataeMtpcWwAAKF6TEb3ngAAUgK3YmU__JMXAEAAwIAA3MAAzYE"
    await message.answer_photo(photo=biz, caption="Biz Ziyo o'quv markazida IT sohasini o'rgatamiz.")


@router.message(F.text == ADDRESS)
async def send_location(message: Message):
    LATITUDE = 41.40926610
    LONGITUDE = 69.30800970
    await message.answer_location(latitude=LATITUDE, longitude=LONGITUDE)
    await message.answer("Ziyo o'quv markazi manzili!")


@router.message(F.text == KURS)
async def send_course_info(message: Message):
    kurs_image = "AgACAgIAAxkBAVnjnGd_4h6qiczFQwYL1xLORs6OPe1eAAJ56TEb3ngAAUj4Upw3661_pgEAAwIAA3MAAzYE"  # Haqiqiy rasm URL sini kiriting yoki fayl id foydalaning.
    await message.answer_photo(photo=kurs_image, caption="Ziyo School kurslari haqida ma'lumot", reply_markup=keyboard)


@router.message(F.text == SAVOL)
async def send_top_5(message: Message):
    await message.answer(text=savol)
    await message.answer(text=TELEGRAPH_LINK)

