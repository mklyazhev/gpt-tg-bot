from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.bot.common import ButtonCallbackFactory


def generate_menu() -> InlineKeyboardMarkup:
    """
    Generates a bot menu keyboard
    :return: Inline keyboard
    """

    buttons = {
        "Новый чат": "/new_chat",
        "Чаты": "/chats",
        "Баланс": "/balance",
        "Настройки": "/settings",
        "Помощь": "/help",
        "Режим разработчика": "/dev"
    }
    builder = InlineKeyboardBuilder()
    for item in buttons.items():
        builder.button(
            text=item[0],
            callback_data=ButtonCallbackFactory(command=item[1]).pack()
        )
    return builder.adjust(2).as_markup()
