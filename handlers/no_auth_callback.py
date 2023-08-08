from logging import info
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_no_auth_menu import menu_keyboard_with_no_auth

router = Router()


@router.callback_query(F.data == 'menu')
async def about_user(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=f"Меню",
        reply_markup=menu_keyboard_with_no_auth.adjust(1).as_markup()
    )
    info('NO_AUTH_MENU_OPENED')
