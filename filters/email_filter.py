import asyncio
from aiogram.filters import BaseFilter
from aiogram.types import Message
from validate_email import validate_email


class IsTrueEmail(BaseFilter):
    async def __call__(self, message: Message):
        # result = await asyncio.to_thread(validate_email(message.text, verify=True))
        if validate_email(message.text) is True:
            return True
        return False
