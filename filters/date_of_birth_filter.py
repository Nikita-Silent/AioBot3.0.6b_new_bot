from aiogram.filters import BaseFilter
from aiogram.types import Message
from time import strptime


class IsTrueDOB(BaseFilter):
    async def __call__(self, message: Message):
        try:
            strptime(message.text, '%d/%m/%Y')
            return True
        except ValueError:
            return False
