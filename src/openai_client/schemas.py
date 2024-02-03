from enum import Enum
from typing import Optional

from langchain_community.chat_models import ChatOpenAI
from pydantic import BaseModel, Field


class SystemPrompt(Enum):
    base = "Ты AI чат-бот ассистент на базе языковой модели GPT компании OpenAI. К тебе обращаются через телеграм бота. Ты должен отвечать на все вопросы, которые тебе задают."


class ModelClient(Enum):
    chat_openai = ChatOpenAI


class ModelSettings(BaseModel):
    model_name: str
    api_url: str
    api_key: str
    temperature: Optional[float] = Field(ge=0, le=1, default=0.7)
    max_tokens: Optional[int] = None
    max_retries: Optional[int] = 2
    request_timeout: Optional[float] = None

    class Config:
        # Установка protected_namespaces для решения конфликта имени "my_model"
        # в классе ModelSetting и родительском классе BaseModel
        protected_namespaces = ()


def prepare_chat_openai_settings(model_settings: dict) -> dict:
    settings = ModelSettings.model_validate(model_settings).model_dump()
    settings["openai_api_base"] = settings.pop("api_url")
    settings["openai_api_key"] = settings.pop("api_key")

    return settings


class SettingsHandler(Enum):
    chat_openai = (prepare_chat_openai_settings,)
