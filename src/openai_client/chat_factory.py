from src.openai_client import Chat
from src.openai_client.schemas import SystemPrompt


class ChatFactory:
    @staticmethod
    def create_chat_openai(model_settings, system_prompt=SystemPrompt.base.value) -> Chat:
        return Chat(model_settings, client_alias="chat_openai", system_prompt=system_prompt)
