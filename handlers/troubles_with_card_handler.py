from random import randint
from aiogram import Router, F, Bot, html
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from filters.chat_type_filter import ChatTypeFilter
from filters.phone_filter import IsTruePhone
from utils.satesform import StepsFormTroublesWithCard
from keyboards.inline_keyboard import move_to_menu, answer_for_final_question
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from config_reader import config
from database.dbconnect import Request

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
cancel_list = ['Отменить', '/cancel', 'отменить', 'ОТМЕНА', 'отмена', 'Отмена', 'jnvtyf', 'cancel']


@router.message(F.text.in_(cancel_list))  # If incorrect answer for previous question
async def cancel_all(message: Message, state: FSMContext):
    await message.answer(
        text=f'Вы {html.bold("отменили")} создание заявки.',
        reply_markup=move_to_menu.adjust(1).as_markup()
    )
    await state.clear()


@router.callback_query(F.data == 'troubles_with_card')
async def cmd_need_help(callback_data: CallbackQuery, state: FSMContext):
    await state.update_data(person_id=callback_data.from_user.id)
    await state.update_data(person_name=callback_data.from_user.username)
    await callback_data.message.answer(
        text=f'{callback_data.from_user.full_name}, мы сожалеем, что у вас возникли проблемы с картой! \n',
        reply_markup=ReplyKeyboardRemove()
    )
    await callback_data.message.answer(
        text=f'Пожалуйста укажите ваш текущий номер в поле "Сообщение" 🔽(внизу)\n'
             f'{html.bold("P.s Это необходимо для того, чтобы в случае возникновения у нас вопросов мы могли связаться с вами")}',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(StepsFormTroublesWithCard.phone_number)


@router.message(StepsFormTroublesWithCard.phone_number, F.text, IsTruePhone())
async def phone_number_written(message: Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    await message.answer(
        text=f'Чтобы мы могли эффективнее работать следуйте пунктам приведенным ниже: \n'
             f'1. Напишите номер телефона, что был привязан к карте с которой возникла проблема.\n'
             f'2. Напишите с чем возникла проблема (отображение дивидендов, не считывается карта на кассе и прочее) \n'
             f'3. Самый важный пункт! Отправльте все одним текстовым сообщением иначе мы увидим только часть \n',
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=html.bold('4.Все вышеперечисленное надо указать в поле "Сообщение" 🔽(внизу)'),
    )
    await state.set_state(StepsFormTroublesWithCard.reason_written)


@router.message(StepsFormTroublesWithCard.phone_number)  # If Check user phone number is NO
async def phone_number_written_incorrect(message: Message):
    await message.answer(
        text=f'Пожалуйста укажите ваш текущий номер правильно \n'
             f'Примеры: +78007009563 , или 88007009563, или 8007009563\n'
             f'P.s Это необходимо для того, чтобы в случае возникновения у нас вопросов мы могли связаться с вами',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(StepsFormTroublesWithCard.reason_written, F.text)
async def request_text_written(message: Message, state: FSMContext):
    await state.update_data(request_text=message.text)
    problem = await state.get_data()
    await message.answer(
        text=f'Вот текст вашей заявки, проверьте правильность заполнения и \n'
             f'Если все правильно нажмите Да на клавиатуре внизу \n'
             f'Если хотите отменить заявку нажмите на Отменить\n'
             f'P.s. Если вы что-то указали неправильно, то пересоздайте заявку\n'
             f'Ваш номер телефона: {problem["phone_number"]}\n'
             f'Описание проблемы: {problem["request_text"]}\n',
        reply_markup=answer_for_final_question.adjust(1).as_markup()
    )
    await state.set_state(StepsFormTroublesWithCard.everything_is_ok_question)


@router.callback_query(StepsFormTroublesWithCard.everything_is_ok_question, F.data == 'answer_for_final_question_yes')
async def answer_is_ok(callback_data: CallbackQuery, bot: Bot, state: FSMContext, request: Request):
    number_of_request = randint(1, 1000000000000)
    problem = await state.get_data()
    await callback_data.message.edit_text(
        text=f'Ваша заявка принята в работу! Ожидайте ответа в ЛС\n',
        reply_markup=move_to_menu.adjust(1).as_markup()
    )
    await bot.send_message(config.main_chat_id,
                           f'Номер заявки: #TroublesWithCard{number_of_request}\n'
                           f'Вопрос задал: @{problem["person_name"]}\n '
                           f'Объект: {problem["phone_number"]}\n '
                           f'Предмет: {problem["request_text"]}\n '
                           f'Статус: ❌ Не решено')

    await request.add_card_trouble_data(number_of_request, problem['person_id'], problem["person_name"],
                                        problem["phone_number"], problem["request_text"], '❌ Не решено')
    await state.clear()


@router.callback_query(StepsFormTroublesWithCard.everything_is_ok_question,
                       F.data == 'answer_for_final_question_cancel')
async def answer_is_cancel(callback_data: CallbackQuery, state: FSMContext):
    await callback_data.message.edit_text(
        text=f'Вы отменили создание заявки.'
    )
    await state.clear()

    await callback_data.message.answer(
        text=f'Чтобы перейти в меню нажмите кнопку внизу',
        reply_markup=move_to_menu.adjust(1).as_markup()
    )


@router.callback_query(StepsFormTroublesWithCard.everything_is_ok_question,
                       F.data == 'answer_for_final_question_recreate')
async def answer_is_rebuild(callback_data: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_data.message.edit_text(
        text=f'Вы пересоздаете заявку.'
    )
    await callback_data.message.answer(
        text=f'{callback_data.from_user.full_name}, мы сожалеем, что у вас возникли проблемы с картой \n'
    )
    await callback_data.message.answer(
        text=f'Пожалуйста укажите ваш текущий номер в поле "Сообщение" 🔽(внизу)\n'
             f'P.s Это необходимо для того, чтобы в случае возникновения у нас вопросов мы могли связаться с вами'
    )
    await state.set_state(StepsFormTroublesWithCard.phone_number)
