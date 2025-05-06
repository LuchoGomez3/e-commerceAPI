from enum import Enum
from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config

# Load .env file based on the environment
current_file_dir = Path(__file__).resolve().parent
env_path = current_file_dir.parent.parent / ".env"
load_dotenv(env_path)

config = Config(str(env_path))


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    APP_NAME: str = config("APP_NAME", default="FastAPI app")
    APP_DESCRIPTION: str = config("APP_DESCRIPTION", default="FastAPI app")
    FRONTEND_URL: str = config("FRONTEND_URL", default="http://localhost:3000")
    BACKEND_URL: str = config("BACKEND_URL", default="https://localhost:8000")


class PostgresSettings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    POSTGRES_PORT: int = config("POSTGRES_PORT", cast=int, default=5432)
    POSTGRES_DB: str = config("POSTGRES_DB", default="postgres")
    POSTGRES_ASYNC_PREFIX: str = config("POSTGRES_ASYNC_PREFIX", default="postgresql+asyncpg")
    POSTGRES_USER: str = config("POSTGRES_USER")
    POSTGRES_PASSWORD: str = config("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = config("POSTGRES_SERVER")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.POSTGRES_SERVER.endswith(":" + str(self.POSTGRES_PORT)):
            self.POSTGRES_SERVER = self.POSTGRES_SERVER.rstrip(":" + str(self.POSTGRES_PORT))
        assert self.POSTGRES_USER is not None, "POSTGRES_USER is required"
        assert self.POSTGRES_PASSWORD is not None, "POSTGRES_PASSWORD is required"

    @property
    def POSTGRES_URI(self) -> str:
        return f"{self.POSTGRES_ASYNC_PREFIX}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    POSTGRES_URL: str | None = config("POSTGRES_URL", default=None)

class EnvironmentOption(str, Enum):
    TEST = "test"
    LOCAL = "local"
    DEVELOP = "dev"
    STAGING = "stg"
    PRODUCTION = "prd"


class EnvironmentSettings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    ENVIRONMENT: EnvironmentOption = config(
        "ENVIRONMENT",
        default=EnvironmentOption.LOCAL,
        cast=lambda x: EnvironmentOption(x),
    )


class Settings(AppSettings, EnvironmentSettings, PostgresSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    pass


settings = Settings()
