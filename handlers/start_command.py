from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.inline_keyboard import builder
from config_reader import config
from handlers.authentication import check_sub_channel
from filters.chat_type_filter import ChatTypeFilter

router = Router()
router.message.filter(
    ChatTypeFilter(chat_type=["private"])
)


@router.message(Command("start"))
async def cmd_start(message: Message, bot: Bot):
    if not check_sub_channel(chat_member=await bot.get_chat_member(config.main_chat_id, message.from_user.id)):
        await message.answer(
            text="Бот перезапущен",
            show_alert=True
        )
        return
    await message.answer(
        text="Подпишись на группу и зарегистрируйся, иначе не получится воспользоваться ботом!",
        reply_markup=builder.adjust(2).as_markup()  # + builder_menu_not_registered
    )



