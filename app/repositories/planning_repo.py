from sqlalchemy.orm import Session
from repositories.base_repo import Repository
from models.planning import Planning
from schemas.planning import PlanningSchema
from utils import format_datetime


class PlanningRepository(Repository):
    async def get_all(self, db: Session):
        return db.query(Planning).all()

    async def get_sorted(self, db: Session, sort_direction: int):
        if sort_direction == 0:
            return db.query(Planning).order_by(Planning.start_date.asc()).all()

        if sort_direction == 1:
            return db.query(Planning).order_by(Planning.start_date.desc()).all()

    async def filter_by_attr(self, db: Session, source_column: str, target_value):
        return db.query(Planning).filter(getattr(Planning, source_column) == target_value).all()

    async def create_plan(self, db: Session, plan: PlanningSchema):
        # print(plan)
        # format_datetime(**plan)
        new_plan = Planning(**plan)
        db.add(new_plan)
        db.commit(new_plan)


planning_repo = PlanningRepository(Planning)
