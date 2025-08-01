
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.models.product_history import ProductHistory

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
    
    def update_box(self, product_id, new_box_id):
        product = repository.get_by_id(product_id)

        if product.box_id != new_box_id:
            history = ProductHistory(
                product=product,
                box_id_before=product.box_id,
                box_id_after=new_box_id
            )
            product.box_id = new_box_id
            return repository.update_box(product, history)
            
        
