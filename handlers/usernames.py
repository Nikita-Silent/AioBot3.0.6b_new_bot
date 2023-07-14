from typing import List

from aiogram import Router, F, Bot
from aiogram.types import Message

from filters.find_usernames import HasUsernamesFilter

from config_reader import config

router = Router()


@router.message(F.text, HasUsernamesFilter())
async def message_with_usernames(message: Message, usernames: List[str], bot: Bot):
    await bot.send_message(config.main_chat_id, f'{", ".join(usernames)} помогите!')
