from logging import info
from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import move_to_menu
from keyboards.inline_auth_menu import menu_keyboard_with_auth
from database.dbconnect import Request
from filters.menu_filter import AuthenticationFilter

router = Router()
router.message.filter(AuthenticationFilter())
router.callback_query.filter(AuthenticationFilter())


@router.callback_query(F.data == 'menu_edit_text')
async def about_user(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=f"Меню",
        reply_markup=menu_keyboard_with_auth.adjust(1).as_markup()
    )
    info('AUTH_MENU_OPENED')


@router.callback_query(F.data == 'menu')
async def about_user(callback_query: CallbackQuery):
    await callback_query.message.answer(
        text=f"Меню",
        reply_markup=menu_keyboard_with_auth.adjust(1).as_markup()
    )
    info('AUTH_MENU_OPENED')


@router.callback_query(F.data == 'about_user')
async def about_user(callback_query: CallbackQuery, request: Request):
    user_data = await request.get_data(callback_query.from_user.id)
    info('about_user')
    await callback_query.message.edit_text(
        text=f"Ваше имя: {user_data[1]}\n"
             f"Ваша фамиллия: {user_data[2]}\n"
             f"Ваша дата рождения: {user_data[5]}\n"
             f"Ваша почта: {user_data[3]}\n"
             f"Ваш номер телефона: {user_data[4]}",
        reply_markup=move_to_menu.adjust(1).as_markup()
    )
