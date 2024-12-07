import pytest
import pytest_asyncio
import asyncio

from aiogram import Bot

from bot.__main__ import main
from bot.dispatcher import BotDispatcher, BOT
from telemipt.databases.tracker_store import TrackerStore

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session", autouse=True)
async def polling():
    yield # suspended until tests are done
    await BOT.close()
    await BotDispatcher.router.stop_polling()

@pytest.fixture()
def rdb() -> type[TrackerStore]:
    return TrackerStore


@pytest.fixture()
def dispatcher() -> type[BotDispatcher]:
    return BotDispatcher


@pytest.fixture()
def bot() -> Bot:
    return BOT

    

