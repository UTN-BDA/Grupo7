
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
    
    def get_by_email(self, email: str ) -> User:
        return repository.get_by_email(email)
    
    def get_users(self, offset, per_page):
        return repository.get_users(offset, per_page)
    
    def search_by_name(self, name):
        return repository.search_by_name(name)
