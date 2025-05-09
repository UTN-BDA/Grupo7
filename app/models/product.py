from datetime import datetime
from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    box_id = db.Column(db.Integer, db.ForeignKey('boxes.id'), nullable=True)

    # Relaciones
    box = db.relationship('Box', back_populates='products')
    history = db.relationship('ProductHistory', back_populates='product', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Product {self.id} - {self.name}>"
