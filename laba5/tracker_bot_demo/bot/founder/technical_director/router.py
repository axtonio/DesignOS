__all__ = ["TechnicalDirector"]

from aiogram import Router

from telemipt.routers.templates import BPMBaseRouter

from ..purchase import *
from .foreman import *

class TechnicalDirector(BPMBaseRouter):
    alias: str = "Технический директор"
    router: Router = Router()
    children: list[type[BPMBaseRouter]] = [Foreman]
    dependent: list[type[BPMBaseRouter]] = [PurchaseRouter, Foreman]
    menu = True
