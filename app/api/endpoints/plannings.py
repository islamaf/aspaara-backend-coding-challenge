from typing import Any
from fastapi import APIRouter, Depends, Request
from fastapi_pagination import Page, paginate, add_pagination, Params
from sqlalchemy.orm import Session

from db.deps import get_db, SessionLocal

from models.planning import Planning
from schemas.planning import PlanningSchema, PlanningCreatedSchema
from repositories.planning_repo import planning_repo

router = APIRouter()
add_pagination(router)


@router.get("/", response_model=Page[PlanningCreatedSchema])
async def plannings(
    db: Session = Depends(get_db),
    pagination_params: Params = Depends()
):
    res = await planning_repo.get_all(db)
    return paginate(res, pagination_params)


@router.get("/sort", response_model=Page[PlanningCreatedSchema])
async def plannings_sort(
    db: Session = Depends(get_db),
    sort_direction: int = 0,
    pagination_params: Params = Depends()
):
    '''
        The sort_direction parameter stands for the sorting of data based on asc (int = 0) and desc (int = 1)
        The pagination_params consist of page and size, used like this in the url "/plannings/sort?page=1&size=15"
    '''

    res = await planning_repo.get_sorted(db, sort_direction)
    return paginate(res, pagination_params)


@router.get("/filter", response_model=Page[PlanningCreatedSchema])
async def plannings_filter(
    request: Request,
    db: Session = Depends(get_db),
    pagination_params: Params = Depends()
):
    '''
        Filtering will depend on the column you choose to filter with, it is not bound to any strict filtering.
        Simply use the query params in the url to indicate the column and the target value in this way:
            "/plannings/filter?id=1" or "/plannings/filter?is_unassigned=0" or any column of your preference.
    '''

    query_param = str(request.query_params).split("&")[0].split("=")
    source_column = query_param[0]
    target_value = query_param[1]

    res = await planning_repo.filter_by_attr(db, source_column, target_value)
    return paginate(res, pagination_params)
