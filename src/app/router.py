from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_async_session
from src.app.schemas import ApiSettings
from src.openai_client.schemas import ModelSettings

router = APIRouter()


@router.post("/set_api_settings")
async def set_api_key(api_settings: ApiSettings, session: AsyncSession = Depends(get_async_session)):
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
async def get_chats(user_id: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = None  # select(Chat).where(Chat.user_id == user_id)
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


@router.get("/get_balance")
async def get_balance(user_id: str, session: AsyncSession = Depends(get_async_session)):
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
