from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import builder_menu_registered, builder_faq
router = Router()


@router.callback_query(F.data == 'faq')
async def faq(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="FAQ",
        reply_markup=builder_faq.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'menu')
async def menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Добро пожаловать в меню бота!",
        reply_markup=builder_menu_registered.adjust(1).as_markup()
    )



