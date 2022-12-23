from models.office import Office
from repositories.base_repo import Repository


class OfficeRepository(Repository):
    ...


office_repo = OfficeRepository(Office)
