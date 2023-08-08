from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsTruePhone(BaseFilter):
    async def __call__(self, message: Message):
        number = message.text
        if len(number) == 12 and number[0] == '+':
            return True
        elif len(number) == 11 and number[0] == '8':
            return True
        elif len(number) == 10 and number[0] == '9':
            return True
        return False
