import asyncio
import json
from pathlib import Path

from db.init_db import init_db
from db.deps import SessionLocal


async def create_db():
    filename = Path(__file__).parent.parent / "planning.json"

    session = SessionLocal()

    with open(filename) as plannings:
        await init_db(session, records=json.load(plannings))
    session.commit()
    session.close()
