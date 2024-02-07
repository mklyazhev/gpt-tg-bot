from pydantic import SecretStr, PostgresDsn, HttpUrl
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    telegram_bot_token: SecretStr

    gpt_api_token: SecretStr
    gpt_api_url: HttpUrl

    db_user: str
    db_password: SecretStr
    db_host: str
    db_port: str
    db_name: str

    logfile: Path

    # использовать этот вариант, когда все будет готово (и для alembic)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    # использовать этот вариант, когда надо протестировать файл из src.openai_client.examples
    # model_config = SettingsConfigDict(env_file=r"../../../.env", env_file_encoding="utf-8")

    @property
    def async_db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password.get_secret_value()}@{self.db_host}:{self.db_port}/{self.db_name}?async_fallback=True"


config = Settings()
