from flask import Blueprint, jsonify
from app.mapping import UserSchema 
from app.services import UserService

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
user_service = UserService()

@user_bp.route('user/<int:user_id>', methods=['GET'])
def get_by_id(user_id: int):
    user = user_service.get_by_id(user_id)
    result = user_schema.dump(user)
    return jsonify(result), 200

