import uvicorn
import asyncio
from fastapi import FastAPI

from core.config import settings
from api.routers import api_router
from create_db import create_db

app = FastAPI(title="aspaara")
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    asyncio.run(create_db())
    # uvicorn.run("main:app")
