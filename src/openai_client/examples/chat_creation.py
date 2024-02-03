from src.openai_client import ChatFactory
from src.config import config

model_settings = {
    "model_name": "gpt-3.5-turbo",
    "api_url": str(config.gpt_api_url),
    "api_key": config.gpt_api_token.get_secret_value(),
}

factory = ChatFactory()
chat = factory.create_chat_openai(model_settings)

while True:
    user_prompt = input()
    print(chat.send_prompt(user_prompt), sep="\n")
