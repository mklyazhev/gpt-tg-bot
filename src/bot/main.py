from pathlib import Path
import asyncio

from fastapi import FastAPI
from loguru import logger
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src import logs_handler
from src.bot import handlers
from src.bot.middlewares import DbSessionMiddleware
from src.config import config


# @app.on_event("startup")
# async def on_startup():
#     await bot.set_webhook(url=WEBHOOK_URL)
#
#     logger.info("App started")
#
#     # Register middlewares
#     dp.update.outer_middleware(ConfigMiddleware(config))
#
#     # Register routes
#     dp.include_router(start_router)
#
#
# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     telegram_update = types.Update(**update)
#     await dp.feed_update(bot=bot, update=telegram_update)
#
#
# @app.on_event("shutdown")
# async def on_shutdown():
#     await bot.session.close()
#     logger.info("App stopped")


async def main() -> None:
    # Включение логирования
    await logs_handler.setup()

    # Инициализация приложения
    app = FastAPI()

    # Подключение к БД
    engine = create_async_engine(url=str(config.async_db_url), echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    # await database.setup()

    # Инициализация экземпляра Bot с режимом парсинга HTML (чтобы не было проблем с экранированием)
    bot = Bot(token=config.telegram_bot_token.get_secret_value(), parse_mode="HTML")
    bot_user = await bot.me()
    logger.info(f"Initialize Bot: {bot_user.full_name} [@{bot_user.username}]")

    ROOT_DIR: Path = Path(__file__).parent.parent
    logger.debug(f'{ROOT_DIR=}')

    # Удаление всех обновлений, которые пришли, когда бот был неактивен.
    # Это нужно, чтобы он обрабатывал только те сообщения,
    # которые пришли непосредственно во время его работы, а не за всё время.
    logger.info("Drop pendings updates")
    await bot.delete_webhook(drop_pending_updates=True)

    # Инициализация экземпляра Dispatcher с хранилищем Redis
    storage = MemoryStorage() # RedisStorage() - сделать так, чтобы в Redis хранился зашифрованный контекст
    dp = Dispatcher(storage=storage)
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # dp.callback_query.middleware(CallbackAnswerMiddleware())
    logger.info(f"Initialize Dispatcher")

    # Инициализация клиента OpenAI
    # client = openai.OpenAI(api_key=config.gpt_api_token.get_secret_value(), base_url=config.gpt_api_url)
    logger.info(f"Initialize OpenAI client")

    # Подключение handler'ов
    logger.info("Configure handlers")
    await handlers.setup(dp)

    # Запуск отслеживания событий
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
