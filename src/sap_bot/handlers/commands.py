from aiogram import types

from src.sap_bot.misc import dp


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer("Hello! I'm Asyncbot.")
 