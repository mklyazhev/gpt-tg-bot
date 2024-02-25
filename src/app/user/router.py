from typing import List

from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy import select, and_, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.db.base import get_async_session
from src.app.db.models import Chat
from src.app.db.query_builder import build_insert, build_select, build_update
from src.app.user.schemas import OpenaiSettings
from src.openai_client.schemas import ModelSettings


router = APIRouter(
    prefix="/user",
    tags=["User"],
)


# Надо сделать так, чтобы в метод передавалась схема UserCreate - ее надо создать
# Вставка была в модель User, а не таблицу "gpt.user", вставлялась схема UserCreate
# То же самое сделать с остальными get-select, post-insert, patch-update, delete-delete методами
# Тогда query_builder будет не нужен
@router.post("/create_user")
async def create_user(user_id: int, username: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = build_insert("gpt.user", {"user_id": user_id, "username": username})
        await session.execute(query)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })


@router.post("/set_api_token")
async def set_api_token(user_id: int, token: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = build_update("gpt.user", {"openai_token": token}, {"user_id": user_id})
        await session.execute(query)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })


@router.delete("/delete_api_token")
async def delete_api_token():
    pass


@router.post("/create_chat")
async def create_chat(model_settings: ModelSettings, session: AsyncSession = Depends(get_async_session)):
    try:
        # Создается чат, созданные чаты хранятся где-то в оперативке и пишутся в БД,
        # возможно есть какой-то паттерн для этого

        # В схеме openai_client есть базовый начальный контекст, надо использовать его во время вставки данных в бд
        query = build_insert("gpt.chat", **model_settings.model_dump())
        await session.execute(query)
        await session.commit()
        return {
            "status": "success",
            "data": None,
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })


@router.get("/get_chat")
async def get_chat(user_id: int, chat_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = build_select("gpt.chat", conditions={"user_id": user_id, "chat_id": chat_id})
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })


@router.get("/get_chats")
async def get_chats(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = build_select("gpt.chat", conditions={"user_id": user_id})
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })


@router.get("/get_token_usage")
async def get_token_usage(user_id: int, chat_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = build_select("gpt.chat", columns="token_usage", conditions={"user_id": user_id, "chat_id": chat_id})
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.mappings().all(),
            "details": None,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": e,
        })
