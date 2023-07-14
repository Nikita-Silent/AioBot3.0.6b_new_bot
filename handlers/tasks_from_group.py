from typing import List
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from middlewares.staff_auntificatemiddlware import StaffAuthenticationMiddleware
from filters.find_request_id import HasRequestIdFilter
from database.dbconnect import Request

router = Router()
router.message.middleware(StaffAuthenticationMiddleware())


@router.message(Command('ban'), F.reply_to_message.as_("replied_message"))  # NE RABOTAET
async def cmd_schedule(message: Message):
    await message.answer(
        text=f'{message.from_user.username},у вас недостаточно прав\n',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command('schedule'))
async def cmd_schedule(message: Message, request: Request):
    group_data = await request.get_group()
    await message.answer(
        text=f'{message.from_user.full_name}, вы выбрали функцию просмотра задач.\n',
        reply_markup=ReplyKeyboardRemove()
    )
    for rec_data in group_data:
        await message.answer(
            text=f'Номер заявки: #mirteck{rec_data[0]}\n'
                 f'Вопрос задал: @{rec_data[2]}\n '
                 f'Объект: {rec_data[3]}\n '
                 f'Предмет: {rec_data[4]}\n '
                 f'Проблема: {rec_data[5]}\n'
                 f'Статус заявки: {rec_data[6]}'
        )


@router.message(Command('task_solved'), F.reply_to_message.as_("replied_message"), HasRequestIdFilter())
async def cmd_task_solved(message: Message, found_request_id: List[str], request: Request, bot: Bot):
    string = ''.join(found_request_id)
    # print(await request.try_to_take(str(found_request_id)))
    request_status = '✅ Выполнено'
    await request.update_data(string[8:], request_status)
    await message.answer(f'Задача {", ".join(found_request_id)} сменила статус на\n{request_status}')
    # [[", ".join(map(str, data)) for data in rec_data] for rec_data in group_data]


@router.message(Command('task_in_progress'), F.reply_to_message.as_("replied_message"), HasRequestIdFilter())
async def cmd_task_solved(message: Message, found_request_id: List[str], request: Request, bot: Bot):
    string = ''.join(found_request_id)
    # print(await request.try_to_take(str(found_request_id)))
    request_status = '⚠ В процессе'
    await request.update_data(string[8:], request_status)
    await message.answer(f'Задача {", ".join(found_request_id)} сменила статус на\n{request_status}')
    # [[", ".join(map(str, data)) for data in rec_data] for rec_data in group_data]