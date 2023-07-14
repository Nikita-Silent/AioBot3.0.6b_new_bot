from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import builder_move_to_menu

router = Router()


@router.callback_query(F.data == 'done')
async def done(callback_query: CallbackQuery):
    await callback_query.answer(text="Спасибо, что подписались на канал и зарегестрировались!", show_alert=True)
    await callback_query.message.edit_text(
        text="Перейти в меню бота",
        reply_markup=builder_move_to_menu.adjust(2).as_markup()
        )


def check_sub_channel(chat_member):
    if chat_member != 'left':
        return True
    else:
        return False
