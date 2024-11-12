__all__ = ["AccountantRouter"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter
from telemipt.commands.templates.tracker import GetDocs

from ..purchase import *


class AccountantRouter(BPMBaseRouter):
    alias: str = "Бухгалтерия"
    router: Router = Router()
    dependent: list[type[BPMBaseRouter]] = [PurchaseRouter]
    menu = True

    commands_be_registered = [GetDocs()]
