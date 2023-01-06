from aiogram import types, Dispatcher
from create_bot import dp, bot

#@dp.message_handler()
async def echo_send(message: types.Message):
    if 'привет' in message.text.lower():
    #if message.text == 'Привет':
        await message.answer('И тебе привет')
    #await message.reply(message.text)
        #await bot.send_message(message.from_user.id, 'И тебе привет')

def register_handlers_other(dp: Dispatcher):
        dp.register_message_handler(echo_send)
