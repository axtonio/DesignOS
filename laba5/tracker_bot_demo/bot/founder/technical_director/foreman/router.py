__all__ = ["Foreman"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter

class Foreman(BPMBaseRouter):
    alias: str = "Прораб"
    router: Router = Router()
    menu = True
