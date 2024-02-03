from aiogram import Dispatcher

from src.bot.handlers.gpt.commands import router


async def setup(dp: Dispatcher):
    # Commands
    dp.include_router(router)
