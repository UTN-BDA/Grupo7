from dataclasses import dataclass

from app import db

from .box import Box


@dataclass(init=False, repr=True, eq=True)
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    name:str = db.Column(db.String(120), unique=False, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    phone: str = db.Column(db.String(40), nullable=True)

    #Relationships
    boxes = db.relationship('Box', back_populates='user', cascade='all, delete-orphan')

