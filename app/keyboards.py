from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Каталог")],
    [KeyboardButton(text="Контакты"), KeyboardButton(text="Корзина")]
],
resize_keyboard=True,
input_field_placeholder="Ярик гэй")

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Youtube", 
                          url="https://exemple.com")]])