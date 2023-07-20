from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import builder_faq, loyal_card_register_menu, \
    start_keyboard_with_no_auth, start_keyboard_with_auth, review_dro_keyboard

router = Router()


@router.callback_query(F.data == 'faq')
async def faq(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="FAQ",
        reply_markup=builder_faq.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'make_a_review')
async def review(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Где Вы хотите оставить отзыв?",
        reply_markup=review_dro_keyboard.adjust(1).as_markup()
    )
# можно навестить мидлварь, которая дает соединение с API MCRM и чекает юзеров


@router.callback_query(F.data == 'loyal_card_question')
async def review(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="💳 У Вас есть карта лояльности? ",
        reply_markup=loyal_card_register_menu.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'menu_no_auth')
async def menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Меню бота",
        reply_markup=start_keyboard_with_no_auth.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'menu_auth')
async def menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Меню бота",
        reply_markup=start_keyboard_with_auth.adjust(1).as_markup()
    )
