from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.db.base import get_async_session
from src.app.db.models import Chat
from src.app.user.schemas import ApiSettings
from src.openai_client.schemas import ModelSettings


router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.post("/set_api_settings")
async def set_api_settings(api_settings: ApiSettings, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = None  # insert(ApiSettings).values(**api_settings.model_dump())
        await session.execute(stmt)
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


@router.post("/create_chat")
async def create_chat(model_settings: ModelSettings, session: AsyncSession = Depends(get_async_session)):
    try:
        # Создается чат, созданные чаты хранятся где-то в оперативке и пишутся в БД,
        # возможно есть какой-то паттерн для этого
        stmt = None  # insert(Operation).values(**operation.model_dump())
        await session.execute(stmt)
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


@router.get("/get_chats")
async def get_chats(user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Chat).where(Chat.user_id == user_id)
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
async def get_token_usage(user_id: int, chat_id: int = None, session: AsyncSession = Depends(get_async_session)):
    try:
        query = None
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
