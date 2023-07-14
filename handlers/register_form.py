from logging import info
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from utils.satesform import StepsForm
from keyboards.replay_keyboard import contact_keyboard
from keyboards.inline_keyboard import builder_re_register, builder_move_to_menu
from database.dbconnect import Request
from filters.contact_filter import IsTrueContact
from filters.date_of_birth_filter import IsTrueDOB
from filters.email_filter import IsTrueEmail


router = Router()


@router.callback_query(F.data == 'register')
async def start_register_form(callback_query: CallbackQuery, state: FSMContext):
    info("Start register state")
    await callback_query.message.answer(
        text=f"Пожалуйста, поделитесь своим контактом",
        reply_markup=contact_keyboard
    )
    await state.set_state(StepsForm.giving_info_about_himself)


@router.message(StepsForm.giving_info_about_himself, IsTrueContact())
async def get_contact(message: Message, state: FSMContext):
    await state.update_data(first_name=message.contact.first_name)
    await state.update_data(last_name=message.contact.last_name)
    await state.update_data(phone_number=message.contact.phone_number)
    await message.answer(
        text=f"Пожалуйста, укажите свою дату рождения: \n"
             f"Пример: 30/12/1990"

    )
    await state.set_state(StepsForm.writing_date_of_birth)


@router.message(Command("cancel"))
@router.message(F.data == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )


# Если введено не правильно, то стейт остается тем же и его не перекидывает на некст стейт
@router.message(StepsForm.giving_info_about_himself)
async def got_contact_incorrect(message: Message):
    await message.answer(
        text=f"Указан <b> не ваш </b> контакт! \n Пожалуйста, укажите свой контакт!"
    )


@router.message(StepsForm.writing_date_of_birth, IsTrueDOB())
async def get_date_of_birth(message: Message, state: FSMContext):
    await state.update_data(date_of_birth=message.text)
    await message.answer(
        text="Пожалуйста, укажите свою почту: \n"
             "Пример: example@mirteck.ru"
    )
    await state.set_state(StepsForm.writing_mail)


# Если введено не правильно, то стейт остается тем же и его не перекидывает на некст стейт
@router.message(StepsForm.writing_date_of_birth)
async def got_date_of_birth_incorrect(message: Message):
    await message.answer(
        text=f"Дата указанна неправильно! Укажите дату рождения в соответствии с примером!"
    )


@router.message(StepsForm.writing_mail, IsTrueEmail())
async def get_mail(message: Message, state: FSMContext, request: Request):
    await state.update_data(mail=message.text)
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы зарегестрировались как:{user_data['first_name']} {user_data['last_name']}\n"
             f"Ваша дата рождения: {user_data['date_of_birth']}\n"
             f"Ваша почта: {user_data['mail']} \n Ваш номер телефона: {user_data['phone_number']}",
        reply_markup=builder_re_register.as_markup()
    )
    await request.add_data(message.from_user.id, user_data['first_name'], user_data['last_name'],
                           user_data['mail'], user_data['phone_number'], user_data['date_of_birth'])
    await message.answer(
        text=f"Если вы закончили реистрацию, то нажмите",
        reply_markup=builder_move_to_menu.as_markup()
    )
    info('Finished register')
    await state.clear()


@router.message(StepsForm.writing_mail)
async def got_mail_incorrect(message: Message):
    await message.answer(text='Идет проверка почты, пожалуйста подожите...')
    await message.answer(
            text="Пожалуйста, укажите свою почту, правильно: \n"
                 "Пример: example@mirteck.ru"
        )

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
