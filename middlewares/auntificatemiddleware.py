from aiogram import BaseMiddleware, Bot
from aiogram.types import TelegramObject
from aiogram.exceptions import TelegramAPIError
from typing import Dict, Any, Awaitable, Callable
from config_reader import config
from contextlib import suppress
from database.dbconnect import Request


class AuthenticationMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        with suppress(TelegramAPIError):
            bot: Bot = data["bot"]
            request: Request = data["request"]
            member = await bot.get_chat_member(
                config.main_chat_id, event.from_user.id
            )
            registered = await request.get_data(event.from_user.id)  # Проверка по бд
            if member.status != "left" and registered is not None:
                return await handler(event, data)
            if member.status != "left" and event.data == 'register':
                return await handler(event, data)
        if member.status == "left":
            await event.answer(
                "Подпишитесь на канал",
                show_alert=True)
        if registered is None:
            await event.answer(
                "Зарегестрируйтесь в боте.",
                show_alert=True
            )
