from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
bot = Bot(token='5634671721:AAHEUlarRhn7t_4atbw73B0-g1-csBHDF6U')
dp = Dispatcher(bot, storage=storage)
