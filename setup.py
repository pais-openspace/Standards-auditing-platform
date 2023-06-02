from aiogram import executor

from src.sap_tg_bot.setting import setting
from src.sap_tg_bot.quiz import Quiz
from src.standarts_auditing_platform import SAP_audit


sap_audit = SAP_audit('templates/config-sample.yaml')

setting.add_quiz(Quiz(1, sap_audit))

from src.sap_tg_bot.main import dp
from src.sap_tg_bot.handlers import *
executor.start_polling(dp, skip_updates=True)


