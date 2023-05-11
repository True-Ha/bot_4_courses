import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from .dataconfig import TOKEN, PAYMENTS_TOKEN

storage = MemoryStorage()

bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage)
