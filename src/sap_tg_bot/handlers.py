from aiogram import types

from .main import dp
from .setting import setting

__all__ = [
    "cmd_start",
    "inline_kb_answer_callback_handler",
    "echo",
    "choose_poll",
    "MENU_STANDARDS",
]

MENU_STANDARDS = 'm_standards'

print(setting.list_quiz)
choose_poll = types.ReplyKeyboardMarkup(resize_keyboard=True)
for quiz in setting.list_quiz:
    choose_poll.add(types.KeyboardButton(text=quiz.sap_audit.standard, callback_data=f'standard-{quiz.quiz_id}'))


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    poll_keyboard.add(types.KeyboardButton("Список стандартов", callback_data=MENU_STANDARDS))
    await message.answer("Выберите доступные для аудита стандарты", reply_markup=poll_keyboard)

# говнокод лютый. нужно исправить

@dp.message_handler(lambda message: message.text == "Список стандартов")
async def inline_kb_answer_callback_handler(message: types.Message):
    print(message.text)
    await message.answer("Доступные стандарты", reply_markup=choose_poll)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text in [quiz.sap_audit.standard for quiz in setting.list_quiz]:
        await message.answer("Начало теста")
    await message.reply(message.text)
