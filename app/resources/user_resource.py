from flask import Blueprint, jsonify, request
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

@user_bp.route("/users/", methods=["GET"])
def get_users():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=50, type=int)

    per_page = min(per_page, 100)

    offset = (page - 1) * per_page

    users = user_service.get_users(offset, per_page)
    schema = UserSchema(many=True)

    return jsonify({
        "page": page,
        "per_page": per_page,
        "results": schema.dump(users)
    })

@user_bp.route("/users/search", methods=["GET"])
def search_users_by_name():
    search = request.args.get("name", default="", type=str).strip()

    if not search:
        return jsonify({"error": "Debes proporcionar un parámetro 'name'"}), 400

    users = user_service.search_by_name(search)
    schema = UserSchema(many=True)

    return jsonify(schema.dump(users)), 200
