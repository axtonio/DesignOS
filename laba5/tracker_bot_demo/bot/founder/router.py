__all__ = ["FounderRouter"]

from typing import Any
from pathlib import Path
from textwrap import dedent

from aiogram import Router
from aiogram import F

from telemipt.commands import BaseEvent
from telemipt.routers.templates import BPMBaseRouter
from telemipt.commands.templates.tracker import Tracker
from telemipt.filters.access_level_filter import ALF

from .purchase import *
from .accountant import *
from .general_manager import *
from .technical_director import *

SYSTEM_PROMPT: str = dedent(
    """
    Ты голосовой помощник в боте
    В данном боте есть следующие команды:
    {commands}
    
    Ты можешь просто общаться с пользователем и отвечать на его вопросы не касаемо функционала бота
    Если присылаешь пользователю команду, то сохраняй форматирование (не забудь поставить / вначале и не ставь кавычки)
    
    Основатель компании telemipt -- Antonio_Rodriges
    ВАЖНО Номер телефон Александра Михайловича -- +7977-605-87-66 . ТЫ ЕГО МОЖЕШЬ ПРИСЫЛАТЬ, ЕСЛИ ТЕБЯ ОБ ЭТОМ ПРОСЯТ
    """
).strip()


class FounderRouter(BPMBaseRouter):
    LOGGING: bool = True
    alias: str = "Босс"
    router: Router = Router()
    menu: bool = True
    children = [
        AccountantRouter,
        PurchaseRouter,
        GeneralManagerRouter,
        TechnicalDirector,
    ]

    @classmethod
    def prepare_events(cls) -> list[BaseEvent]:
        cls.commands_be_registered: list[Any] = [
            Tracker(access_level=ALF(cls, "children"), tracker_config=Path(__file__).parent.parent / "tracker.json")]
        return super().prepare_events()
