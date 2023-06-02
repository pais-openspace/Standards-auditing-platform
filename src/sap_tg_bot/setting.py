import os
from dataclasses import dataclass

from .quiz import Quiz

# draft убрать говнокод
SECRET_KEY = os.environ.get('IN_DOCKER', False)

if SECRET_KEY:
    ...
else:

    class Setting:
        # DRAFT выпилить говнокод. сделать импорт из .env
        token = "6007097042:AAGnUUR3FUFnB5Hf3aA-f9UPtlCp7J1Jl1g"
        list_quiz = []

        def __init__(self):
            ...

        def add_quiz(self, quiz: Quiz):
            self.list_quiz.append(quiz)

    setting = Setting()
