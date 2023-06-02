import logging
from aiogram import Bot, Dispatcher, executor

from .setting import setting

logging.basicConfig(level=logging.INFO)

bot = Bot(token=setting.token)
dp = Dispatcher(bot)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
