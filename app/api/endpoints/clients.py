from typing import Any
from fastapi import APIRouter, Depends, Request
from fastapi_pagination import Page, paginate, add_pagination, Params
from sqlalchemy.orm import Session

from db.deps import get_db, SessionLocal

from models.client import Client
from repositories.client_repo import client_repo
from schemas.client import ClientSchema

router = APIRouter()


@router.post("/new")
async def create(
    client: ClientSchema,
    db: Session = Depends(get_db),
):
    return await client_repo.create_client(db, client)


@router.post("/delete/{id}")
async def delete(
    id: str,
    db: Session = Depends(get_db)
):
    return await client_repo.delete_client_by_id(db, id)


@router.patch("/update")
async def update(
    client: ClientSchema,
    db: Session = Depends(get_db)
):
    return await client_repo.update_client(db, client)
