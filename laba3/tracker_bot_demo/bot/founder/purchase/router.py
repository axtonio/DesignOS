__all__ = ["PurchaseRouter"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter

from .sub_purchase import *


class PurchaseRouter(BPMBaseRouter):
    alias: str = "Закупка"
    children: list[type[BPMBaseRouter]] = [SubPurchaseRouter]
    router: Router = Router()
    menu = True
