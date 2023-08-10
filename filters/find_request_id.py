from typing import Union, Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.dbconnect import Request


class HasRequestIdFilter(BaseFilter):
    async def __call__(self, message: Message, request: Request) -> Union[bool, Dict[str, Any]]:
        entities = message.reply_to_message.entities or []
        found_request_id = [item.extract_from(message.reply_to_message.text)
                            for item in entities if item.type == "hashtag"]
        list_of_request_numbers = []
        for i in await request.get_all_request_troubles_with_card():
            # Пролетаем по полученному Record и переносим в список
            list_of_request_numbers.append(f'#TroublesWithCard{i[0]}')
        # Если команды есть, то "проталкиваем" их в хэндлер
        # по имени "found_commands"
        if ''.join(found_request_id) in list_of_request_numbers:
            return {"found_request_id": found_request_id}
        return False
