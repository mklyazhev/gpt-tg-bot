from aiogram.filters.callback_data import CallbackData


class ButtonCallbackFactory(CallbackData, prefix="button"):
    command: str
