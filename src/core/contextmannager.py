from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.DB.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Initialize the database engine and create tables
    engine, session_local = init_db()
    app.state.session_local = session_local
    app.state.engine = engine

    # Yield control back to FastAPI (app is running)
    yield

    # Shutdown: Clean up, if necessary (e.g., close engine)
    await engine.dispose()
