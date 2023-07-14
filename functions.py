from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.inline_keyboard import builder, builder_menu_registered
from config_reader import config
from handlers.authentication import check_sub_channel
from database.dbconnect import Request

router = Router()


@router.message(Command(commands=["menu", "start"]))
@router.message(Text(text="меню", ignore_case=True))
async def cmd_start(message: Message, bot: Bot, state: FSMContext, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await state.clear()
    if check_sub_channel(chat_member=await bot.get_chat_member(config.main_chat_id, message.from_user.id)):
        # and await check_user(user_id=message.from_user.id) is not None:
        await message.answer(
            text="Меню бота",
            reply_markup=builder_menu_registered.adjust(2).as_markup()  # + builder_menu_registered
        )
        return
    await message.answer(
        text="Подпишись на группу и зарегестрируйся, иначе не получится воспользоваться ботом!",
        reply_markup=builder.as_markup()  # + builder_menu_not_registered
    )
    return


@router.message(Command(commands=["cancel"]))
@router.message(Text(text="отмена", ignore_case=True))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Действие отменено",
        reply_markup=ReplyKeyboardRemove()
    )
