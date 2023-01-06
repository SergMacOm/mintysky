#import asyncio
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards import kb_client
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import time
import tg_analytic

kb_gor = InlineKeyboardMarkup(row_width=3)
kb_gor_oven = InlineKeyboardButton(text='Овен', callback_data='oven')
kb_gor_telec = InlineKeyboardButton(text='Телец', callback_data='telec')
kb_gor_bliznecy = InlineKeyboardButton(text='Близнецы', callback_data='bliznecy')
kb_gor_rak = InlineKeyboardButton(text='Рак', callback_data='rak')
kb_gor_lev = InlineKeyboardButton(text='Лев', callback_data='lev')
kb_gor_deva = InlineKeyboardButton(text='Дева', callback_data='deva')
kb_gor_vesi = InlineKeyboardButton(text='Весы', callback_data='vesi')
kb_gor_skorpion = InlineKeyboardButton(text='Скорпион', callback_data='skorpion')
kb_gor_strelec = InlineKeyboardButton(text='Стрелец', callback_data='strelec')
kb_gor_kozerog = InlineKeyboardButton(text='Козерог', callback_data='kozerog')
kb_gor_vodolei = InlineKeyboardButton(text='Водолей', callback_data='vodolei')
kb_gor_ribi = InlineKeyboardButton(text='Рыбы', callback_data='ribi')


kb_gor.add(kb_gor_oven, kb_gor_telec, kb_gor_bliznecy)
kb_gor.add(kb_gor_rak, kb_gor_lev, kb_gor_deva)
kb_gor.add(kb_gor_vesi, kb_gor_skorpion, kb_gor_strelec)
kb_gor.add(kb_gor_kozerog, kb_gor_vodolei, kb_gor_ribi)

class OrderStone(StatesGroup):
    waiting_for_stone_name = State()
    


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Вас приветствует компания MintySky', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n https://t.me/mintyskybot')

#@dp.message_handler(commands=['Оформить_заказ'])
async def command_sait(message: types.Message):
    tg_analytic.statistics(message.chat.id,message.text) 
    await bot.send_message(message.from_user.id, 'https://mintysky.ru/')

#@dp.message_handler(commands=['Написать_нам'])
async def command_post(message: types.Message):
    tg_analytic.statistics(message.chat.id,message.text) 
    await bot.send_message(message.from_user.id, 'welcome@mintysky.ru')

#@dp.message_handler(commands=['Узнать_о_камне'])
async def command_stone(message: types.Message):
    tg_analytic.statistics(message.chat.id,message.text) 
    await bot.send_message(message.from_user.id, 'Напишите название камня')
    await OrderStone.waiting_for_stone_name.set()

async def stone_chosen(message: types.Message, state: FSMContext):
    
    await state.update_data(chosen_stone=message.text.lower())
    

    if 'опал' in message.text.lower():
        with open("stone/opal.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'малахит' in message.text.lower():
        with open("stone/malahit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'турмалин' in message.text.lower():
        with open("stone/tyrmalin.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'аквамарин' in message.text.lower():
        with open("stone/akvamarin.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'аметист' in message.text.lower():
        with open("stone/ametist.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'чароит' in message.text.lower():
        with open("stone/charoit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'цитрин' in message.text.lower():
        with open("stone/citrin.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'гранат' in message.text.lower():
        with open("stone/granat.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'иолит' in message.text.lower():
        with open("stone/iolit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'изумруд' in message.text.lower():
        with open("stone/izymryd.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'кионит' in message.text.lower():
        with open("stone/kianit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'кварц' in message.text.lower():
        if 'розовый' not in message.text.lower():
            with open("stone/kvarc.txt") as file:
                  for item in file:
                       await bot.send_message(message.from_user.id, item)
            await state.finish()
    elif 'лабрадорит' in message.text.lower():
        with open("stone/labradorit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'лазурит' in message.text.lower():
        with open("stone/lazyrit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'лунный' and 'камень' in message.text.lower():
        with open("stone/lyn_kam.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'оливин' in message.text.lower():
        with open("stone/olivin.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'розовый' and 'кварц' in message.text.lower():
        with open("stone/roz_kvarc.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'сапфир' in message.text.lower():
        with open("stone/sapfir.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()

    elif 'танзанит' in message.text.lower():
        with open("stone/tanzanit.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish()
    elif 'топаз' in message.text.lower():
        with open("stone/topaz.txt") as file:
              for item in file:
                   await bot.send_message(message.from_user.id, item)
        await state.finish() 
    else:
        await bot.send_message(message.from_user.id, 'Попробуйте еще раз. Нажмите Узнать_о_камне')
        await state.finish()
#@dp.message_handler(commands=['Гороскоп'])
async def command_goroskop(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выберите знак зодиака', reply_markup=kb_gor)



@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    if 'oven' in call.data:
        await call.message.answer('Овен - сапфир, рубин, турмалин')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/oven.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'telec' in call.data:
        await call.message.answer('Телец - Дымчатый кварц, Гранат, Иолит')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/telec.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif 'bliznecy' in call.data:
        await call.message.answer('Телец - Дымчатый кварц, Гранат, Иолит')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/blizneci.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif 'rak' in call.data:
        await call.message.answer('Рак - Изумруд, Аквамарин, Опал')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/rak.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif 'lev' in call.data:
        await call.message.answer('Лев -Цитрин, Опал, Гранат')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/lev.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif 'deva' in call.data:
        await call.message.answer('Дева -Сапфир, Аметист, Иолит')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/deva.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'vesi' in call.data:
        await call.message.answer('Весы - Лунный камень, Аметист, Розовый кварц')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/vesi.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'skorpion' in call.data:
        await call.message.answer('Скорпион - Топаз, Цитрин, Турмалин')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/skorpion.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'strelec' in call.data:
        await call.message.answer('Стрелец - Сапфир, Бирюза, Турмалин')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/strelec.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'kozerog' in call.data:
        await call.message.answer('Козерог - Топаз, Дымчатый кварц, Турмалин')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/kozerog.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'vodolei' in call.data:
        await call.message.answer('Водолей - Сапфир, Аметист, Аквамарин')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/vodolei.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
    elif 'ribi' in call.data:
        await call.message.answer('Рыбы - Лунный камень, Топаз, Опал')
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('Gor/riba.jpg'))
        await call.message.answer_media_group(media=media)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'], state="*")
    dp.register_message_handler(command_sait, commands=['Оформить_заказ'], state="*")
    dp.register_message_handler(command_post, commands=['Написать_нам'], state="*")
    dp.register_message_handler(command_stone, commands=['Узнать_о_камне'], state="*")
    dp.register_message_handler(command_goroskop, commands=['Гороскоп'], state="*")
    dp.register_message_handler(stone_chosen, state=OrderStone.waiting_for_stone_name)
