from aiogram import Router, F
import httpx
from aiogram.types import CallbackQuery, BufferedInputFile
from filters.chat_type_filter import ChatTypeFilter
from api_connections.qr_api import payload, headers, url
from keyboards.inline_keyboard import loyal_card_register_menu,  review_dro_keyboard, loyal_card_menu_keyboard, \
                                      question_menu, builder_faq, move_to_menu

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.callback_query(F.data == 'ask')
async def ask(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=f"❓ {callback_query.from_user.first_name}, выберите что Вы хотите",
        reply_markup=question_menu.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'faq')
async def faq(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=f"❓ Часто задаваемые вопросы",
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
async def loyal_card_question(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="💳 У Вас есть карта лояльности? ",
        reply_markup=loyal_card_register_menu.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'loyal_card_menu')
async def loyal_card_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text=f"💳 {callback_query.from_user.first_name}, выберите что вы хотите",
        reply_markup=loyal_card_menu_keyboard.adjust(1).as_markup()
    )


@router.callback_query(F.data == 'get_share_qr')
async def loyal_card_menu(callback_query: CallbackQuery):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            photo = BufferedInputFile(response.content, filename='qr_mirteck')
            await callback_query.message.answer_photo(photo=photo, caption='Ваш QR для создания карты лояльности')
        else:
            print('Ошибка при выполнении запроса:', response.status_code)

