from datetime import datetime, timezone

from app import db


class Box(db.Model):
    __tablename__ = 'boxes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda:datetime.now(timezone.utc))

    # Relaciones
    user = db.relationship('User', back_populates='boxes')
    products = db.relationship('Product', back_populates='box', cascade='all, delete-orphan')
    histories = db.relationship('ProductHistory', back_populates='box_after', foreign_keys='ProductHistory.box_id_after')

    def __repr__(self):
        return f"<Box {self.id} - {self.name}>"
