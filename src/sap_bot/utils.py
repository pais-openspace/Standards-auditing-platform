from aiogram.types import poll
from aiogram import Bot

from src.standarts_auditing_platform.sap_quiz import SAP_audit, SAP_question


def get_new_audit():
    return SAP_audit('templates/config-sample.yaml')


def generate_progress_bar(progress):
    bar_length = 20
    filled_length = int(bar_length * progress)
    empty_length = bar_length - filled_length
    bar = '█' * filled_length + '-' * empty_length * 2
    percentage = f"{progress:.0%}"
    progress_bar = f"[{bar}] {percentage}"
    return progress_bar


class Quiz:
    _audit = 0

    def __init__(self):
        self.sapa = get_new_audit()
        self._audit = self.sapa.start()

    def next(self):
        try:
            return self._audit.__next__()
        except StopIteration as e:
            print(e)
            return -1, -1

    def answer(self, id, quest, answer):
        self.sapa.answer(id, quest, answer)
        print([(x, x.answer) for x in self.sapa.fields])

    def is_end(self):
        return self.sapa.is_end
