from app.models.user import User
from app import db

class UserRepository:

    def save(self, user):
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()

    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_all(self):
        return User.query.all()

    def get_users(self, offset, per_page):
        return User.query.offset(offset).limit(per_page).all()
    
    def search_by_name(self, name):
        return User.query.filter(User.name.ilike(f"%{name}%")).all()
