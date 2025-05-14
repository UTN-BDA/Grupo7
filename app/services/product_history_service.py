
from app.models.product_history import ProductHistory
from app.repositories.product_history_repository import \
    ProductHistoryRepository

repository = ProductHistoryRepository()

class ProductHistoryService:

    def __init__(self) -> None:
        None

    def save(self, product_history: ProductHistory) -> ProductHistory:
        return repository.save(product_history)
    
    def delete(self, product_history: ProductHistory) -> None:
        repository.delete(product_history)
    
    def get_by_id(self, id: int) -> ProductHistory:
        return repository.get_by_id(id)
    
    def get_by_product(self, product_id: int) -> ProductHistory:
        return repository.get_by_product(product_id)