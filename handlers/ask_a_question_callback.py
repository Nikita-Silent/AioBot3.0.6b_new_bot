from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import builder_ask_a_question
from middlewares.workhours_middleware import OfficeHoursMiddleware

router = Router()
router.callback_query.middleware(OfficeHoursMiddleware())


@router.callback_query(F.data == 'ask_a_question')
async def ask_a_question(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="Задать вопрос",
        reply_markup=builder_ask_a_question.adjust(1).as_markup()
    )
