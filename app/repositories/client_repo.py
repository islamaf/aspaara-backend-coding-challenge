from sqlalchemy.orm import Session
from models.client import Client
from repositories.base_repo import Repository
from schemas.client import ClientSchema


class ClientRepository(Repository):
    async def create_client(self, db: Session, client):
        new_client = ClientSchema(
            id=client.id,
            name=client.name
        )
        await self.add_get_record(db, Client, **new_client.dict())
        db.commit()
        return new_client

    async def delete_client_by_id(self, db: Session, id):
        effected_rows = db.query(Client).filter_by(id=id).delete()

        if effected_rows == 0:
            return "No clients found by this id"
        else:
            db.commit()
            return f'Client {id} is now deleted'

    async def update_client(self, db: Session, update_client):
        client = db.query(Client).filter_by(id=update_client.id)
        client.name = update_client.name
        db.commit()
        return "Updated client"


client_repo = ClientRepository(Client)
