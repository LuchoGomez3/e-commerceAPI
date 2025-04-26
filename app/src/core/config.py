from enum import Enum
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

class EnvironmentOption(str, Enum):
    TEST = "test"
    LOCAL = "local"
    DEVELOP = "dev"
    STAGING = "stg"
    PRODUCTION = "prd"


class EnvironmentSettings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    ENVIRONMENT: EnvironmentOption = config(
        "ENVIRONMENT", default=EnvironmentOption.LOCAL, cast=lambda x: EnvironmentOption(x)
    )

class Settings(AppSettings, EnvironmentSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    pass


settings = Settings()