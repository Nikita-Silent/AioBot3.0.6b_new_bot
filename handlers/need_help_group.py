from random import randint
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from filters.chat_type_filter import ChatTypeFilter
from utils.satesform import StepsFormGroup
from keyboards.replay_keyboard import make_row_keyboard
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from middlewares.staff_auntificatemiddlware import StaffAuthenticationMiddleware
from config_reader import config
from database.dbconnect import Request

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
router.message.middleware(StaffAuthenticationMiddleware())

shop = ['Л32', 'Л90', 'Л98', 'Н22', 'О49', 'П13', 'С6', 'С39']
problem_object = ['Касса', 'Принтер', 'Компьютер', 'ТСД', 'ДРУГОЙ']


@router.message(Command('help'))
async def cmd_need_help(message: Message, state: FSMContext):
    await state.update_data(person_id=message.from_user.id)
    await state.update_data(person_name=message.from_user.username)
    await message.answer(
        text=f'{message.from_user.full_name}, вы выбрали функцию помощи.\n'
             f'Пожалуйста, выберите магазин, где возникла проблема: ',
        reply_markup=make_row_keyboard(shop)
    )
    await state.set_state(StepsFormGroup.shop_chosen)


@router.message(StepsFormGroup.shop_chosen, F.text.in_(shop))
async def shop_chosen(message: Message, state: FSMContext):
    await state.update_data(shop=message.text)
    await message.answer(
        text=f'Выберите объект с которым возникли проблемы',
        reply_markup=make_row_keyboard(problem_object)
    )
    await state.set_state(StepsFormGroup.problem_object_chosen)


@router.message(StepsFormGroup.shop_chosen)
async def shop_chosen_incorrect(message: Message):
    await message.answer(
        text=f'Пожалуйста, выберите магазин, где возникла проблема: ',
        reply_markup=make_row_keyboard(shop)
    )


@router.message(StepsFormGroup.problem_object_chosen, F.text.in_(problem_object))
async def problem_object_chosen(message: Message, state: FSMContext):
    await state.update_data(problem_object=message.text)
    await message.answer(
        text=f'Опишите кратко проблему:',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(StepsFormGroup.reason_written)


@router.message(StepsFormGroup.problem_object_chosen)
async def problem_object_chosen_incorrect(message: Message):
    await message.answer(
        text='Выберите из представленного ниже',
        reply_markup=make_row_keyboard(problem_object)
    )


@router.message(F.text, StepsFormGroup.reason_written)
async def written_problem(message: Message, bot: Bot, state: FSMContext, request: Request):
    number_of_request = randint(1, 1000000000000)
    await state.update_data(written_problem=message.text)
    problem = await state.get_data()
    await message.answer(
        text=f'Ваша заявка принята в работу! Ожидайте ответа в ЛС\n',
        reply_markup=ReplyKeyboardRemove()
    )
    await bot.send_message(config.main_chat_id,
                           f'Номер заявки: #mirteck{number_of_request}\n'
                           f'Вопрос задал: @{problem["person_name"]}\n '
                           f'Объект: {problem["shop"]}\n '
                           f'Предмет: {problem["problem_object"]}\n '
                           f'Проблема: {problem["written_problem"]}\n'
                           f'Статус: ❌ Не решено')

    await request.add_group_data(number_of_request, problem['person_id'], problem["person_name"],
                                 problem["shop"], problem["problem_object"], problem["written_problem"], '❌ Не решено')
    await state.clear()
