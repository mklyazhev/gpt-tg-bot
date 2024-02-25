from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field, SecretStr


class User(BaseModel):
    user_id: int
    username: str
    openai_token: str
    is_admin: bool
    is_blocked: bool
    date_create: datetime


class Chat(BaseModel):
    chat_id: int
    user_id: int
    summary: str
    context: str
    token_usage: int
    date_create: datetime


class OpenaiSettings(BaseModel):
    # Вроде как больше не нужно, но разобраться перед тем как удалять
    pass
