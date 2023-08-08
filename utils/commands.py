from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats, BotCommandScopeAllGroupChats


async def set_commands(bot: Bot):
    commands_for_private = [
        BotCommand(
            command="start",
            description="Начало работы/Перезапуск бота"
        ),
        BotCommand(
            command="cancel",
            description="Отменить текущее действие"
        )
    ]
    commands_for_group = [
        BotCommand(
            command="schedule",
            description="Текущие заявки"
        ),
        BotCommand(
            command="task_solved",
            description='Перевести заявку в статус "✅ Выполненные"'
        ),
        BotCommand(
            command="task_in_progress",
            description='Перевести заявку в статус "⚠ В работе"'
        )
    ]
    await bot.set_my_commands(commands_for_group, BotCommandScopeAllGroupChats())
    await bot.set_my_commands(commands_for_private, BotCommandScopeAllPrivateChats())
