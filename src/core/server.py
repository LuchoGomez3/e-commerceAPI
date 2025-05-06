from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import EnvironmentOption, settings
from core.router import get_global_router
from core.contextmannager import lifespan

def create_fastapi_app() -> FastAPI:

    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        port=8000,
        reload=True if settings.ENVIRONMENT != EnvironmentOption.PRODUCTION else False,
        workers=1,
        lifespan=lifespan,
    )

    # Cors conf
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(get_global_router(), prefix="/api")

    return app
