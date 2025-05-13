from app.models.product_history import ProductHistory
from app import db

class ProductHistoryRepository:

    def save(self, history):
        db.session.add(history)
        db.session.commit()
        return history

    def delete(self, history):
        db.session.delete(history)
        db.session.commit()

    def get_by_id(self, history_id):
        return ProductHistory.query.get(history_id)

    def get_by_product(self, product_id):
        return ProductHistory.query.filter_by(product_id=product_id).order_by(ProductHistory.timestamp.desc()).all()


