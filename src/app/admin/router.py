from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.db.base import get_async_session

router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
)


@router.post("/ban_user")
async def ban_user(user_id: str, session: AsyncSession = Depends(get_async_session)):
    pass


@router.post("/unban_user")
async def unban_user(user_id: str, session: AsyncSession = Depends(get_async_session)):
    pass


@router.get("/get_tokens_usage")
async def get_tokens_usage(user_id: str, session: AsyncSession = Depends(get_async_session)):
    pass
