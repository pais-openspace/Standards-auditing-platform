from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from src.sap_bot.misc import dp, bot


@dp.message_handler(commands=['test'])
async def test(msg: types.Message):
    await bot.send_poll(
        chat_id=msg.chat.id,
        question="Кто ты?",
        options=["1. sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdf", '2. dfffffffffffffffffffffffffffffffffffffffffffffffffffff',
                 '3 ghgggggggggggggggggggggggggggggggggggggggg'],
        type="regular",
        allows_multiple_answers=True,
        is_anonymous=False,
        correct_option_id=[0, 3],
        explanation='wow 1'
    )


@dp.poll_answer_handler()
async def handle_poll_answer(poll: types.PollAnswer):
    ans = poll.option_ids
    print(poll)
    await bot.send_message(poll.user.id, ans)
