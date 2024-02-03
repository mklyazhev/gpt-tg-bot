from aiogram import Dispatcher
# from aiogram.dispatcher.filters import CommandStart, Text

from src.bot.handlers.user.commands import router


async def setup(dp: Dispatcher):
    # Commands
    dp.include_router(router)
