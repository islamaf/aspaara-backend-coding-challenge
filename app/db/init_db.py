from datetime import datetime
from typing import List

from db.session import Base, engine
from sqlalchemy.orm import Session

from utils import format_datetime

from models.planning import Planning
from models.client import Client
from models.manager import JobManager
from models.office import Office
from models.talent import Talent

from schemas.planning import PlanningSchema, PlanningCreatedSchema
from schemas.client import ClientSchema
from schemas.manager import JobManagerSchema
from schemas.office import OfficeSchema
from schemas.talent import TalentSchema

from repositories.planning_repo import PlanningRepository, planning_repo
from repositories.client_repo import ClientRepository, client_repo
from repositories.manager_repo import ManagerRepository, manager_repo
from repositories.office_repo import OfficeRepository, office_repo
from repositories.talent_repo import TalentRepository, talent_repo


tables = [Planning, Client, Talent, Office, JobManager]


async def init_db(session: Session, records: List[dict]):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    for record in records:
        format_datetime(record)
        init_planning = PlanningSchema(**record)

        client_record = ClientSchema(
            id=init_planning.client_id,
            name=init_planning.client_name
        )

        await client_repo.add_get_record(session, Client, **client_record.dict())

        if init_planning.job_manager_id:
            job_manager_record = JobManagerSchema(
                id=init_planning.job_manager_id,
                name=init_planning.job_manager_name
            )

            await manager_repo.add_get_record(session, JobManager, **job_manager_record.dict())

        if init_planning.talent_id:
            talent_record = TalentSchema(
                id=init_planning.talent_id,
                name=init_planning.talent_name,
                grade=init_planning.talent_grade
            )

            await talent_repo.add_get_record(session, Talent, **talent_record.dict())

        office_record = OfficeSchema(
            city=init_planning.office_city,
            postal_code=init_planning.office_postal_code
        )

        await office_repo.add_get_record(session, Office, **office_record.dict())

        planning_record = PlanningCreatedSchema(**init_planning.dict())
        await planning_repo.add_get_record(session, Planning, **planning_record.dict())
