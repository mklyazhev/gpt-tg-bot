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


class ApiSettings(BaseModel):
    pass
