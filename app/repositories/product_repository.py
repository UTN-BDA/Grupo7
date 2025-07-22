from app import db
from app.models.product import Product
from app.models.product_history import ProductHistory
from datetime import datetime

class ProductRepository:
    def get_by_id(self, product_id):
        return Product.query.get(product_id)

    def get_by_box(self, box_id):
        return Product.query.filter_by(box_id=box_id).all()

    def save(self, product: Product):
        db.session.add(product)
        db.session.commit()
        return product

    def delete(self, product):
        db.session.delete(product)
        db.session.commit()

    def update_box(self, product, history):
        db.session.add(product)
        db.session.add(history)
        db.session.commit()
        return product
