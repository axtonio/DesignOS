import asyncio

# Получение директории, в которой находится файл скрипта
from terminal_app.env import source
from terminal_app.logging import register_logger

source(".tracker_bot.env")

from datalchemy.scheduler import SCHEDULER

from .dispatcher import *


async def main():

    # SCHEDULER.start()

    await BOT.delete_webhook(drop_pending_updates=True)

    await BotDispatcher.start_polling(BOT)


if __name__ == "__main__":
    register_logger(name="aiogram.dispatcher", library=True)
    register_logger(name="aiogram.webhook", library=True)
    register_logger(name="aiogram.middlewares", library=True)
    register_logger(name="aiogram.scene", library=True)
    register_logger(name="aiogram.event", library=True)

    try:
        asyncio.run(main())
    finally:
        print("Bot closed")
