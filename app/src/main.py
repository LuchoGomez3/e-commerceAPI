import uvicorn
from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(
        app="core.server:create_fastapi_app",
        host="localhost",
        reload=True,
        workers=1,
        factory=True
    )