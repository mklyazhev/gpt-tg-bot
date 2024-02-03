import openai
from aiogram import Router, flags
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionMiddleware

from loguru import logger

from src.config import config

router = Router(name="gpt-commands-router")
router.message.middleware(ChatActionMiddleware())


@router.message(Command("new_chat"))
@flags.chat_action(initial_sleep=0, action="typing", interval=0)
async def cmd_new_chat_handler(message: Message) -> None:
    client = openai.OpenAI(api_key=config.gpt_api_token.get_secret_value(), base_url=str(config.gpt_api_url))

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Поприветствуем же друг друга!"}],
        stream=False,
    )

    answer = chat_completion.choices[0].message.content
    logger.info(chat_completion) # доделать логирование успешных/неуспешных ответов
    await message.answer(answer, parse_mode="MARKDOWN", disable_web_page_preview=True)


@router.message(Command("chats"))
async def cmd_chats_handler(message: Message) -> None:
    pass
