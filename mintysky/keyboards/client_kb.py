from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Оформить_заказ')  
b2 = KeyboardButton('/Написать_нам')
b3 = KeyboardButton('/Узнать_о_камне')
b4 = KeyboardButton('/Гороскоп')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
#kb_client.add(b1).add(b2).add(b3).add(b4)
kb_client.add(b1,b2).add(b3,b4)
