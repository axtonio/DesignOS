__all__ = ["SubPurchaseRouter"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter


class SubPurchaseRouter(BPMBaseRouter):
    alias: str = "Отдел снабжения"
    router: Router = Router()
    menu = True
