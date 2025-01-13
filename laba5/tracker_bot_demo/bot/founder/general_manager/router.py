__all__ = ["GeneralManagerRouter"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter

from ..purchase import *
from ..accountant import * 
from ..technical_director import *


class GeneralManagerRouter(BPMBaseRouter):
    alias: str = "Генеральный директор"
    router: Router = Router()
    dependent: list[type[BPMBaseRouter]] = [
        PurchaseRouter,
        AccountantRouter,
        TechnicalDirector,
    ]
    menu = True
