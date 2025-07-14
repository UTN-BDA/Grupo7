from flask import Blueprint, jsonify, request

from app.mapping import BoxSchema
from app.services import BoxService

box_bp = Blueprint('box', __name__)
box_schema = BoxSchema()
box_service = BoxService()

@box_bp.route('box/create_box', methods=['POST'])
def create_box():
    #Leer valores del json 
    box = box_schema.load(request.json)
    box = box_service.create_box(box)
    #Comprobar si se creo la caja
    if box.id:
        status_code = 200
    else:
        status_code = 500
    return box_schema.dump(box), status_code
@box_bp.route('box/by_user/<int:user_id>', methods=['GET'])
def get_by_user(user_id: int):
    # Obtener todas las boxes del usuario
    boxes = box_service.get_by_user(user_id)
    # Serializar muchos registros con many=True
    schema= BoxSchema(many= True)
    result = schema.dump(boxes)
    return jsonify(result), 200

@box_bp.route('box/box_id/<int:id>', methods=['GET'])
def get_by_id(id: int):
    # Obtener un box por su id
    box = box_service.get_by_id(id)
    # Serializar muchos registros con many=True
    #schema = BoxSchema(many=False)
    result = box_schema.dump(box)
    return jsonify(result), 200