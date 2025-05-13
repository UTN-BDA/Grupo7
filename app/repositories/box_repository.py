from app import db
from app.models import Box

class BoxRepository:
    def get_by_id(self, box_id):
        return Box.query.get(box_id)

    def get_by_user(self, user_id):
        return Box.query.filter_by(user_id=user_id).all()

    def save(self, box):
        db.session.add(box)
        db.session.commit()
        return box

    def delete(self, box):
        db.session.delete(box)
        db.session.commit()
