from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URL: Optional[str] = "sqlite:///planning.db"

    class Config:
        case_sensitive = True


settings = Settings()
