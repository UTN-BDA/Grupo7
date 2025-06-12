
from app.models.box import Box
from app.repositories.box_repository import BoxRepository

repository = BoxRepository()

class BoxService:

    def __init__(self) -> None:
        None

    def save(self, box: Box) -> Box:
        return repository.save(box)
    
    def delete(self, box: Box) -> None:
        repository.delete(box)
    
    def get_by_id(self, id: int) -> Box:
        return repository.get_by_id(id)
    
    def get_by_user(self, user_id: int) -> Box:
        return repository.get_by_user(user_id)