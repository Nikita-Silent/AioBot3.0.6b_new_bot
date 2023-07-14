from datetime import datetime
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Dict, Any, Awaitable, Callable


def office_hours() -> bool:
    return datetime.now().weekday() in (0, 1, 2, 3, 4) and datetime.now().hour in ([i for i in range(9, 18)])


class OfficeHoursMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.counter = 0

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if office_hours():
            return await handler(event, data)

        await event.answer(
            "Наш сотрудник не может ответить вам, обратитесь в рабочее время с 9:00 до 18:00 по времени Новосибирска ",
            show_alert=True
        )
