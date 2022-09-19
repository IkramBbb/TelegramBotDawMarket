import aiogram.utils.exceptions
from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text


async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Assalawma Aleykum DawMarket Botina Xosh Keldin`iz\nIltimas tildi saylan`', reply_markup=kb_client)
        await message.delete()
    except aiogram.utils.exceptions.Unauthorized:
        await message.reply('https://t.me/DawMarketBot')


async def market_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, '1-kun, 2-kun, 3-kun')


async def market_place_command(message: types.Message):
    await message.reply('A. Dabilov b/n')


async def market_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(market_menu_command, Text(equals='Меню', ignore_case=True))
    dp.register_message_handler(market_place_command, Text(equals='Тех поддержка', ignore_case=True))
    dp.register_message_handler(market_open_command, Text(equals='О нас', ignore_case=True))
