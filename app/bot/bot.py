import os
import django
# import sys
from aiogram.utils import executor




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()
# sys.path.append("/Users/claimixmail.ru/Desktop/fit_bot_may/config/config")


from app.bot.create_bot import dp
from app.bot.handlers import register_handlers


async def on_startup(_):
    print('Bot online')

register_handlers(dp)

executor = executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
