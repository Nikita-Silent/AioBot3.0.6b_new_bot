from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject
from aiogram.exceptions import TelegramAPIError
from typing import Dict, Any, Awaitable, Callable
from config_reader import config
from contextlib import suppress


class StaffAuthenticationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        with suppress(TelegramAPIError):
            bot: Bot = data["bot"]
            member_of_channel = await bot.get_chat_member(
                config.main_chat_id, event.from_user.id
            )
            if member_of_channel.status != "left":
                return await handler(event, data)

