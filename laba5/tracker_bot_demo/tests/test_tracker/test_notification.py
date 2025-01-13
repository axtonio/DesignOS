from aiogram import Bot
from datetime import datetime, timedelta

from terminal_app.types import random_day, random_string

from telemipt.databases.schemas.tracker import TGUser
from telemipt.databases.tracker_store import TrackerStore
from telemipt.routers.templates.redis_router import RedisStoreBaseRouter


class TestNotification:
    async def test_notification(
        self, rdb: type[TrackerStore], dispatcher: type[RedisStoreBaseRouter], bot: Bot
    ):
        # random.choice(list(dispatcher.all_children_alias))

        for _ in range(40):

            rdb(TGUser(user_id=596334818)).insert_task(
                {
                    "from_user": "596334818",
                    "parent": "отдел снабжения",
                    "task_type": "REQUEST",
                    "child": [
                        {
                            "node_id": 0,
                            "router": "босс",
                            "request": "CHECK",
                            "back_id": None,
                            "dependent_id": None,
                            "request_media": ["any"],
                            "subscribers": ["отдел снабжения", "закупка"],
                        },
                        {
                            "node_id": 1,
                            "router": "закупка",
                            "request": "EXECUTE",
                            "back_id": None,
                            "dependent_id": 0,
                            "request_media": ["photo", "document"],
                            "subscribers": ["технический директор", "босс"],
                        },
                        {
                            "node_id": 2,
                            "router": "технический директор",
                            "request": "EXECUTE",
                            "back_id": None,
                            "dependent_id": 1,
                            "request_media": ["document", "text"],
                            "subscribers": ["босс", "закупка"],
                        },
                        {
                            "node_id": 3,
                            "router": "босс",
                            "request": "CHECK",
                            "back_id": 1,
                            "dependent_id": 2,
                            "request_media": ["any"],
                            "subscribers": ["технический директор", "закупка"],
                        },
                        {
                            "node_id": 4,
                            "router": "бухгалтерия",
                            "request": "EXECUTE",
                            "back_id": None,
                            "dependent_id": 3,
                            "request_media": [],
                            "subscribers": [],
                        },
                        {
                            "node_id": 5,
                            "router": "отдел снабжения",
                            "request": "EXECUTE",
                            "back_id": None,
                            "dependent_id": 4,
                            "request_media": ["photo", "document"],
                            "subscribers": ["бухгалтерия", "закупка"],
                        },
                    ],
                    "deadline": random_day(
                        datetime.now().date() - timedelta(days=3), datetime.now().date()
                    ),
                    ":input_media": True,
                    "media_content": [],
                    "text": random_string(),
                    "creation_time": "2024-10-28 04:37:21",
                }
            )
