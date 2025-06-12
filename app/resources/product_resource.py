from flask import Blueprint, jsonify
from app.mapping.product_schema import ProductSchema
from app.services.product_service import ProductService

product_bp = Blueprint('product', __name__)
product_service = ProductService()
product_schema = ProductSchema(many=True)  # Porque puede haber varios productos por box

@product_bp.route('/product/by_box/<int:box_id>', methods=['GET'])
def get_by_box(box_id: int):
    products = product_service.get_by_box(box_id)
    result = product_schema.dump(products)
    return jsonify(result), 200