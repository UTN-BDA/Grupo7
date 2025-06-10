from flask import Blueprint, jsonify
from app.mapping import ProductHistorySchema
from app.services import ProductHistoryService

product_history_bp = Blueprint('product_history', __name__)
product_history_schema = ProductHistorySchema()
product_history_service = ProductHistoryService()

@product_history_bp.route('product_history/<int:product_id>', methods=['GET'])
def get_product_histories(product_id: int):
    # Obtener todos los historiales de productos
    histories = product_history_service.get_by_product(product_id)

    # Serializar muchos registros con many=True
    schema = ProductHistorySchema(many=True)
    result = schema.dump(histories)

    return jsonify(result), 200