
from app.models.user import User
from app.repositories.user_repository import UserRepository

repository = UserRepository()

class UserService:

    def __init__(self) -> None:
        None

    def save(self, user: User) ->User:
        return repository.save(user)
    
    def delete(self, user: User) -> None:
        repository.delete(user)
    
    def get_by_id(self, id: int) -> User:
        return repository.get_by_id(id)
    
    def get_by_username(self, username: str ) -> User:
        return repository.get_by_product(username)