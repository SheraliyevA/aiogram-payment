import logging

from aiogram import Dispatcher
from data.config import ADMINS
from aiogram.types import message

async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"Bot ishga tushdi ")

        except Exception as err:
            logging.exception(err)
