from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


client_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

button_test = KeyboardButton('/Тест')

client_keyboard.add(button_test)
