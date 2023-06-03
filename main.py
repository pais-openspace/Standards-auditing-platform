import sys

from aiogram import Dispatcher

from src.sap_bot import handlers
from src.sap_bot.misc import executor


def main():
    executor.start_polling()


if __name__ == "__main__":
    main()