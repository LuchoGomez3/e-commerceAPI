import uvicorn

from core.config import EnvironmentOption, settings

if __name__ == "__main__":
    
    uvicorn.run(
        app="core.server:create_fastapi_app",
        host="0.0.0.0",
        reload=settings.ENVIRONMENT != EnvironmentOption.PRODUCTION,
        workers=1,
        factory=True
    )
