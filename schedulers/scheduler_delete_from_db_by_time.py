from aiogram import Bot


async def delete_tasks_from_db(bot: Bot):
    await bot.send_message(1046116124, 'Сообщение по таймеру')
