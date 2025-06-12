
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

repository = ProductRepository()

class ProductService:

    def __init__(self) -> None:
        None

    def save(self, product: Product) -> Product:
        return repository.save(product)
    
    def delete(self, product: Product) -> None:
        repository.delete(product)
    
    def get_by_id(self, id: int) -> Product:
        return repository.get_by_id(id)
    
    def get_by_box(self, box_id: int) -> Product:
        return repository.get_by_box(box_id)