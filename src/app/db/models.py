from sqlalchemy import (
    Column, ForeignKey, PrimaryKeyConstraint,
    Integer, BigInteger, Float,
    String, Boolean, DateTime, JSON,
    func
)
from sqlalchemy.dialects import postgresql

from src.app.db import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "gpt"}

    user_id = Column(BigInteger, primary_key=True, unique=True)
    username = Column(String(255), nullable=False)
    openai_token = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)
    is_blocked = Column(Boolean, default=False)
    date_create = Column(DateTime, default=func.now(), nullable=False)


class Chat(Base):
    __tablename__ = "chat"
    __table_args__ = (
        PrimaryKeyConstraint("user_id", "chat_id"),
        {"schema": "gpt"}
    )

    chat_id = Column(Integer, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("gpt.user.user_id"), nullable=False)
    summary = Column(String(512))
    context_json = Column(JSON, nullable=False)
    date_create = Column(DateTime, default=func.now(), nullable=False)
    token_usage = Column(Float(5).with_variant(postgresql.FLOAT, "postgresql"), nullable=False)
