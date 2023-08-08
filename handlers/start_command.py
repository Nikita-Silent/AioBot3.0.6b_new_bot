from logging import info
from aiogram import Router, html
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.inline_auth_menu import menu_keyboard_with_auth
from keyboards.inline_no_auth_menu import menu_keyboard_with_no_auth
from filters.chat_type_filter import ChatTypeFilter
from filters.menu_filter import AuthenticationFilter


router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.message(Command("start"), AuthenticationFilter())  # команда начала бота
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=f'Добро пожаловать в столицу текстильных идей {html.bold("МИРТЕК")}!',
        reply_markup=menu_keyboard_with_auth.adjust(1).as_markup()
    )
    info('AUTH_START')


@router.message(Command("start"))  # команда начала бота
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text=f'Добро пожаловать в столицу текстильных идей {html.bold("МИРТЕК")}!',
        reply_markup=menu_keyboard_with_no_auth.adjust(1).as_markup()
    )
    info('NO_AUTH_START')


