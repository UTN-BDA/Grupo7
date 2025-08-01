from datetime import datetime, timezone

from app import db


class ProductHistory(db.Model):
    __tablename__ = 'product_histories'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    box_id_before = db.Column(db.Integer, db.ForeignKey('boxes.id'), nullable=True)
    box_id_after = db.Column(db.Integer, db.ForeignKey('boxes.id'), nullable=True)
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relaciones
    product = db.relationship('Product', back_populates='history')
    box_before = db.relationship('Box', foreign_keys=[box_id_before])
    box_after = db.relationship('Box', foreign_keys=[box_id_after])
 
    def get_action(self) -> str:
        if self.box_id_before is None and self.box_id_after is not None:
            return "Agregado"
        elif self.box_id_before is not None and self.box_id_after is None:
            return "Eliminado"
        else:
            return "Movido"

    def __str__(self) -> str:
        return f"{self.get_action()} el {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
