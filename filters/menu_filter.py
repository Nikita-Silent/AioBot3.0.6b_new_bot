from aiogram.filters import BaseFilter
from aiogram.types import TelegramObject
from aiogram.exceptions import TelegramAPIError
from typing import Union, Dict, Any
from contextlib import suppress
from database.dbconnect import Request


class AuthenticationFilter(BaseFilter):
    async def __call__(self, event: TelegramObject, request: Request) -> Union[bool, Dict[str, Any]]:
        with suppress(TelegramAPIError):
        #  registered = await request.get_data(event.from_user.id)  # Проверка по бд
            registered = True
        if registered is None:
            return False
        return True
