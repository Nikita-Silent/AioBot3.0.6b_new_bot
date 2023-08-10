import asyncio
import logging
import asyncpg

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from schedulers.scheduler_delete_from_db_by_time import delete_tasks_from_db
from config_reader import config
from handlers import start_command, register_form, callbacks, ask_a_question_callback, \
    need_help_group, tasks_from_group, auth_callback, no_auth_callback, troubles_with_card_handler

from utils.commands import set_commands

from middlewares.dbmiddleware import DbSession
# from middlewares.auntificatemiddleware import AuthenticationMiddleware


async def create_pool():
    return await asyncpg.create_pool(config.postgres_dsn, command_timeout=60)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    pool_connect = await create_pool()
    storage = RedisStorage.from_url(config.redis_dsn)
    dp = Dispatcher(storage=storage)
#    dp.callback_query.middleware.register(AuthenticationMiddleware())
    dp.update.middleware.register(DbSession(pool_connect))
    bot = Bot(config.bot_token.get_secret_value(),  parse_mode="HTML")

    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(delete_tasks_from_db, trigger='interval', seconds=10, kwargs={'bot': bot})

    dp.include_router(auth_callback.router)
    dp.include_router(no_auth_callback.router)
    dp.include_router(start_command.router)
    dp.include_router(ask_a_question_callback.router)
    dp.include_router(callbacks.router)
    dp.include_router(troubles_with_card_handler.router)
    dp.include_router(register_form.router)
#    dp.include_router(usernames.router)
    dp.include_router(need_help_group.router)
    dp.include_router(tasks_from_group.router)

    await set_commands(bot)
    # scheduler.start()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
