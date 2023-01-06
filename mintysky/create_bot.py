import config
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
#from aiogram.contrib.middlewares.logging import LoggingMiddleware


bot = Bot(config.token)
#dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot, storage=MemoryStorage())
#dp.middleware.setup(LoggingMiddleware())
