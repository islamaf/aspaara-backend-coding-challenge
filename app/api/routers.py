from fastapi import APIRouter

from api.endpoints import plannings, clients

api_router = APIRouter()
api_router.include_router(
    plannings.router, prefix="/plannings", tags=["plannings"])
api_router.include_router(
    clients.router, prefix="/clients", tags=["clients"])
