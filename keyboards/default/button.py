from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utlis.static.keyboards import ABOUT_US, ADDRESS, KURS, SAVOL, ADMIN, NUM, LOC

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text=ABOUT_US),
        KeyboardButton(text=ADDRESS),
    ],
    [
        KeyboardButton(text=KURS),
        KeyboardButton(text=SAVOL),
        KeyboardButton(text=ADMIN)
    ],
    [
        KeyboardButton(text=NUM, request_contact=True),
        KeyboardButton(text=LOC, request_location=True),
    ]
])