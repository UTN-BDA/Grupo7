from flask import Blueprint, jsonify, request, send_file
from io import BytesIO
from app.mapping.product_schema import ProductSchema
from app.services.product_service import ProductService
from app.services.product_image_service import ProductImageService

product_bp = Blueprint('product', __name__)
product_service = ProductService()
product_schema = ProductSchema(many=True)  # Porque puede haber varios productos por box
image_service = ProductImageService()

@product_bp.route('/product/by_box/<int:box_id>', methods=['GET'])
def get_by_box(box_id: int):
    products = product_service.get_by_box(box_id)
    result = product_schema.dump(products)
    return jsonify(result), 200

@product_bp.route('/product', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        product = ProductSchema().load(data)
        created = product_service.save(product)
        return jsonify({
            'message': 'Producto creado correctamente'
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@product_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = product_service.get_by_id(product_id)
    if not product:
        return jsonify({'error': 'Producto no encontrado'}), 404

    product_service.delete(product)
    return jsonify({'message': 'Producto eliminado correctamente'}), 200

@product_bp.route('/product/<int:product_id>/image', methods=['POST'])
def upload_image(product_id):
    if 'file' not in request.files:
        return jsonify({"error": "No se envió ningún archivo"}), 400

    file = request.files['file']
    image_service.save_image(
        product_id=product_id,
        image_data=file.read(),
        filename=file.filename,
        content_type=file.content_type
    )
    return jsonify({"message": "Imagen guardada con éxito"}), 201


@product_bp.route('/product/<int:product_id>/image', methods=['GET'])
def get_image(product_id):
    image_doc = image_service.get_image(product_id)
    if not image_doc:
        return jsonify({"error": "Imagen no encontrada"}), 404

    return send_file(
        BytesIO(image_doc['image_data']),
        mimetype=image_doc['content_type'],
        download_name=image_doc['filename']
    )

@product_bp.route('/product/<int:product_id>/image', methods=['DELETE'])
def delete_image(product_id):
    deleted = image_service.delete_image(product_id)
    if deleted:
        return jsonify({"message": "Imagen eliminada con éxito"}), 200
    else:
        return jsonify({"error": "No se encontró imagen para eliminar"}), 404
