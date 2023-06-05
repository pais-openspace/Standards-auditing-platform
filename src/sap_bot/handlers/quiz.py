from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from src.sap_bot.misc import dp, bot
from src.sap_bot.utils import get_new_audit, Quiz, generate_progress_bar
from src.standarts_auditing_platform import SAP_question
from src.standarts_auditing_platform.sap_quiz import A_field



quiz: Quiz = None

current_quiz = ()  # id, quest, answer


@dp.message_handler(commands=['test'])
async def test(msg: types.Message):
    global current_quiz, quiz
    quiz = Quiz()
    await msg.answer(f'Начало аудита...\nТекущий стандарт: {quiz.sapa.standard}\nРаботу выполнил: тут косяк из за вложенности\nОписание: {quiz.sapa.definition}')


    i, quest = quiz.next()
    current_quiz = (i, quest)
    if isinstance(quest, A_field):
        await msg.answer(f'{quest.name}, {quest.value}')
    elif isinstance(quest, SAP_question):
        await bot.send_poll(
            chat_id=msg.chat.id,
            question=quest.text,
            options=[
                x for x in quest.options
            ],
            type="regular",
            allows_multiple_answers=True,
            is_anonymous=False,
            correct_option_id=quest.true_selected,
            explanation='wow 1'
        )


@dp.message_handler()
async def quiz_answer(msg: types.Message):
    global current_quiz, quiz
    if quiz.is_end():
        await msg.answer('Аудит завершен. Желаете скачать отчет?')
        return

    if isinstance(current_quiz[1], A_field):
        value = msg.text
        await msg.answer('Ваш ответ учтен')
        quiz.answer(current_quiz[0], current_quiz[1], value)
        print(quiz.sapa.is_end)

        i, quest = quiz.next()
        current_quiz = (i, quest)
        if isinstance(quest, A_field):
            await msg.answer(f'{quest.name}, {quest.value}')
        elif isinstance(quest, SAP_question):
            print(quest.options)
            await msg.answer('Правильный ответ' + f'{quest.true_selected}')
            await bot.send_poll(
                chat_id=msg.chat.id,
                question=quest.text,
                options=[
                    str(x['value']) for x in quest.options
                ],
                type="regular",
                allows_multiple_answers=True,
                is_anonymous=False,
                correct_option_id=quest.true_selected,
                explanation='wow 1'
            )


@dp.poll_answer_handler()
async def handle_poll_answer(poll: types.PollAnswer):
    global current_quiz, quiz

    if quiz.is_end():
        await bot.send_message(poll.user.id, 'Аудит завершен. Желаете скачать отчет?')
        return

    ans = poll.option_ids
    print(poll)
    await bot.send_message(poll.user.id, 'Следующий вопрос')
    quiz.answer(current_quiz[0], current_quiz[1], ans)
    print(quiz.sapa.is_end)

    i, quest = quiz.next()
    if i == -1:
        # Закончен
        await bot.send_message(poll.user.id, 'Аудит закончен. Получите отчет')

        # Вот тут текст html. Его нужно отправить пользователю
        with open('output.html', 'w') as file:
            file.write(quiz.sapa.report())
        await bot.send_message(poll.user.id, generate_progress_bar(quiz.sapa.score))
        await bot.send_document(poll.user.id, document=open("output.html", "rb"))
        return
    current_quiz = (i, quest)
    if isinstance(quest, SAP_question):
        await bot.send_poll(
            chat_id=poll.user.id,
            question=quest.text,
            options=[
                str(x['value']) for x in quest.options
            ],
            type="regular",
            allows_multiple_answers=True,
            is_anonymous=False,
            correct_option_id=quest.true_selected,
            explanation='wow 1'
        )
