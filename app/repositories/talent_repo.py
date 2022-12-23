from models.talent import Talent
from repositories.base_repo import Repository


class TalentRepository(Repository):
    ...


talent_repo = TalentRepository(Talent)
