from datetime import datetime
from operator import itemgetter
from typing import Any

from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models import ChatOpenAI
from langchain_core.language_models import BaseChatModel
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

from src.openai_client.schemas import ModelClient, SettingsHandler, prepare_chat_openai_settings


class Chat:
    def __init__(self, model_settings: dict, client_alias: str, system_prompt: str):
        self.summary = None
        self.context = ConversationBufferMemory(return_messages=True)
        self.date_create = datetime.now()
        self.__model = self.__create_model(model_settings, client_alias)

        self.__system_prompt = system_prompt
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="history"),
                ("human", "{input}"),
            ]
        )
        self.chain = (
                RunnablePassthrough.assign(
                    history=RunnableLambda(self.context.load_memory_variables) | itemgetter("history")
                )
                | self.prompt_template
                | self.__model
        )

    @staticmethod
    def __create_model(model_settings, client_alias) -> BaseChatModel:  # -> лучше использовать Any или BaseChatModel?
        # Сделать как-нибудь посимпатичнее
        settings = SettingsHandler[client_alias].value[0](model_settings)
        model = ModelClient[client_alias].value(**settings)

        return model

    def __set_summary(self) -> None:
        self.summary = ""

    def send_prompt(self, prompt: str) -> str:
        inputs = {"input": prompt}
        response = self.chain.invoke(inputs)

        self.context.save_context(inputs, {"output": response.content})

        return response.content
