from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from src.bot.keyboards import generate_menu

router = Router(name="user-commands-router")


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = f"""
👋 Привет, *{message.from_user.full_name}*!

С помощью меня ты можешь отправлять запросы ChatGPT прямо здесь, в Телеграме, без использования VPN и браузера!
"""

    await message.answer(text, reply_markup=generate_menu(), parse_mode="MARKDOWN", disable_web_page_preview=True)


@router.message(Command("menu"))
async def cmd_menu_handler(message: Message) -> None:
    text = """
Отправляйте запросы ChatGPT прямо в Telegram!

Выберите одну из следующих опций:
"""
    await message.answer(text, reply_markup=generate_menu(), parse_mode="MARKDOWN", disable_web_page_preview=True)


@router.message(Command("gen_image"))
async def cmd_gen_image_handler(message: Message) -> None:
    pass


@router.message(Command("chats"))
async def cmd_chats_handler(message: Message) -> None:
    pass


@router.message(Command("images"))
async def cmd_images_handler(message: Message) -> None:
    pass


@router.message(Command("balance"))
async def cmd_balance_handler(message: Message) -> None:
    pass


@router.message(Command("help"))
async def cmd_help_handler(message: Message) -> None:
    pass


# @router.message()
# @flags.chat_action(initial_sleep=0, action="typing", interval=0)
# async def echo_handler(message: Message) -> None:
#     """
#     Handler will forward receive a message back to the sender
#
#     By default, message handler will handle all message types (like a text, photo, sticker etc.)
#     """
#     try:
#         # Send a copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")
