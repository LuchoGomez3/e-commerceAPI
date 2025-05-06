from typing import AsyncGenerator
from fastapi import Request
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings


async def get_async_db(request: Request) -> AsyncGenerator[AsyncSession, None]:
    async with request.app.state.session_local() as session:
        yield session

def init_db():
    """
    Initializes the database engine and sessionmaker.
    This function should be called in main.py during server startup.
    """
    engine = create_async_engine(
        settings.POSTGRES_URI,
        future=True,
        echo=True
    )
    session_local = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    return engine, session_local

