from aiogram import Router, Bot, html
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline_keyboard import start_keyboard_with_no_auth
from config_reader import config
from handlers.authentication import check_sub_channel
from filters.chat_type_filter import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.message(Command("start"))  # команда начала бота
async def cmd_start(message: Message):
    await message.answer(
        text=f'Добро пожаловать в столицу текстильных идей {html.bold("МИРТЕК")}!',
        reply_markup=start_keyboard_with_no_auth.adjust(1).as_markup()
    )



