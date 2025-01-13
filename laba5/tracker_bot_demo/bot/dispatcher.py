__all__ = ["BotDispatcher", "BOT"]

from pathlib import Path

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.client.default import DefaultBotProperties

from telemipt.configs import CONFIG
from telemipt.routers import BaseRouter
from telemipt.formatting import TGFormatting
from telemipt.commands.templates import Cancel, Help
from telemipt.commands import BaseEvent, MessageObject
from telemipt.routers.templates import RedisStoreBaseRouter
from telemipt.commands.templates.dev import DevStart, DevExit
from telemipt.commands.templates.tracker.notification import Notification
from telemipt.middlewares import (
    AccessLevelMiddleware,
    ThrottlingMiddleware,
    AlbumMiddleware,
    ParamsMiddleware,
)

from telemipt.media import TELEMIPT_BLUE_BACKGROUND

from .founder import *


class BotDispatcher(RedisStoreBaseRouter):
    alias: str = "Телеграм бот"
    router: Dispatcher = Dispatcher(
        storage=RedisStorage.from_url(
            url=str(CONFIG.redis), connection_kwargs={"decode_responses": True}
        )
    )
    # TODO forget register router (link with transition)
    children: list[type[BaseRouter]] = [FounderRouter]
    commands_be_registered: list[BaseEvent] = [
        Help(
            event_message=f"Активизируйте свой кабинет\n\nЕсли забыли пароль {TGFormatting.MDASH} свяжитесь с {TGFormatting.ANTONIO}"
        ),
        Cancel(),
        DevExit(),
        DevStart(
            message=MessageObject(
                text=f"Вы зашли в демонстрационного бота для постановки и контроля выполнения задач от компании {TGFormatting.italic(TGFormatting.code("Telemipt"))}\n\nЧтобы пройти обучение свяжитесь с {TGFormatting.ANTONIO}\n\nВы можете сами попробовать разобраться и оценить удобство постановки задач, для этого нажмите на {TGFormatting.command("boss")}, в левом нижнем углу у вас появится меню. Далее советуем ввести команду {TGFormatting.command("menu")}\n\nОднако о всем функционале самостоятельно вы не сможете узнать, с вами свяжется {TGFormatting.ANTONIO}",
                media_content=[TELEMIPT_BLUE_BACKGROUND],
            )
        ),
    ]
    transition_commands_instruction = [
        (DevStart("boss", check_username=True), [FounderRouter]),
        (DevStart("ac", check_username=True), [AccountantRouter]),
        (DevStart("gm", check_username=True), [GeneralManagerRouter]),
        (DevStart("pu", check_username=True), [PurchaseRouter]),
        (DevStart("su", check_username=True), [SubPurchaseRouter]),
        (DevStart("td", check_username=True), [TechnicalDirector]),
        (DevStart("fo", check_username=True), [Foreman]),
    ]

    # TODO! You cannot move registration to the base class, otherwise it will be registered several times and it will be bad
    @classmethod
    def register_middlewares(cls) -> None:
        cls.router.message.outer_middleware(ThrottlingMiddleware())
        cls.router.message.outer_middleware(
            AccessLevelMiddleware(router_alias=cls.alias, chat_types=["private"])
        )
        cls.router.callback_query.outer_middleware(
            AccessLevelMiddleware(router_alias=cls.alias, chat_types=["private"])
        )
        cls.router.inline_query.outer_middleware(
            AccessLevelMiddleware(router_alias=cls.alias)
        )

        cls.router.message.middleware(AlbumMiddleware())
        cls.router.message.middleware(ParamsMiddleware())
        cls.router.message.middleware(ParamsMiddleware())
        cls.router.callback_query.middleware(ParamsMiddleware())


BOT = Bot(
    CONFIG.bot_token.get_secret_value(),
    default=DefaultBotProperties(parse_mode="HTML"),
)

# Notification(BOT, BotDispatcher, "default", Path(__file__).parent / "tracker.json")
