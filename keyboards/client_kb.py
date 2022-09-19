from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Меню')
b2 = KeyboardButton('Тех поддержка')
b3 = KeyboardButton('О нас')
b4 = KeyboardButton('Share my number', request_contact=True)
b5 = KeyboardButton('Geolocation', request_location=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).row(b4, b5)
