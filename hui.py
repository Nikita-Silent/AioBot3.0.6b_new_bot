from logging import info
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from utils.satesform import StepsFrom_Group
from time import strptime
from keyboards.replay_keyboard import make_row_keyboard, contact_keyboard
from keyboards.inline_keyboard import builder_re_register, builder_move_to_menu
from validate_email import validate_email
from database.dbconnect import Request


router = Router()


@router.callback_query(F.data == 'register')
async def get_form_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(StepsFrom_Group.GET_LAST_NAME)
    info("Start register state")
    await state.update_data(first_name=callback_query.from_user.first_name)
    await state.update_data(last_name=callback_query.from_user.last_name)
    await callback_query.message.edit_text(
        text=f"Ваше имя: {callback_query.from_user.first_name}\n Ваша фамилия: {callback_query.from_user.last_name}\n"
        f"Телефон"

    )


@router.message(StepsFrom_Group.GET_LAST_NAME)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(StepsFrom_Group.GET_PHONE)
    await message.answer(
        text=f"Ваше имя: {message.from_user.first_name}\n Ваша фамилия: {message.from_user.last_name}\n"
        f"Пожалуйста, укажите свою дату рождения: \n"
             f"Пример: 30/12/1990",
        reply_markup=contact_keyboard
    )


@router.message(StepsFrom_Group.GET_PHONE)
async def get_age(message: Message, state: FSMContext):
    await state.set_state(StepsFrom_Group.GET_AGE)
    try:
        strptime(message.text, '%d/%m/%Y')
    except ValueError:
        await message.answer(
            "Вы неправильно указали свою дату рождения! \n"
            "Пожалуйста, укажите правильно. Пример: 30/12/1990"
        )
        return get_age
    await state.update_data(date_of_birth=message.text)
    await message.answer(
        text="Пожалуйста, укажите свою почту: \n"
             "Пример: example@mirteck.ru"
    )


@router.message(StepsFrom_Group.GET_AGE)
async def get_mail(message: Message, state: FSMContext, request: Request):
    await state.set_state(StepsFrom_Group.GET_INFO)
    await message.answer(text='Идет проверка почты, пожалуйста подожите...')
    if not validate_email(message.text):  # Verify your email , verify=True
        await message.answer(
            text="Пожалуйста, укажите свою почту, правильно: \n"
                 "Пример: example@mirteck.ru"
        )
        return get_mail
    await state.update_data(mail=message.text)
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы зарегестрировались как:{user_data['first_name']} {user_data['last_name']}\n"
             f"Ваша дата рождения: {user_data['date_of_birth']}\n"
             f"Ваша почта: {user_data['mail']}",
        reply_markup=builder_re_register.as_markup()
    )
    await request.add_data(message.from_user.id, message.from_user.first_name)
    info('Finished register')
    await message.answer(
        text=f"Если вы закончили реистрацию, то нажмите",
        reply_markup=builder_move_to_menu.as_markup()
    )
    await state.clear()

# Отмена регистрации убрана до реализации мидлвари проверки на подписку и регистрацию
"""@router.callback_query(F.data == 'cancel_register')
async def cancel_handler(callback_query: CallbackQuery, state: FSMContext, bot: Bot) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return

    info("Cancelling state %r", current_state)
    await state.clear()
    if not check_sub_channel(chat_member=await bot.get_chat_member(config.main_chat_id,
                                                                   callback_query.message.from_user.id)):
        await callback_query.message.edit_text(
            "Регистрация отменена.",
            reply_markup=builder_move_to_menu.as_markup()
        )"""
