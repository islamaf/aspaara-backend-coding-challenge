from models.manager import JobManager
from repositories.base_repo import Repository


class ManagerRepository(Repository):
    ...


manager_repo = ManagerRepository(JobManager)
