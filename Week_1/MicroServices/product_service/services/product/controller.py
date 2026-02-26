from flask import Blueprint, jsonify, request
from .service import ProductService

product_bp = Blueprint('product', __name__, url_prefix='/products')
service = ProductService()


@product_bp.route('/', methods=['GET'])
def list_products():
    prods = service.all()
    return jsonify([p.__dict__ for p in prods])


@product_bp.route('/<int:prod_id>', methods=['GET'])
def get_product(prod_id):
    prod = service.get(prod_id)
    if not prod:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(prod.__dict__)


@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.get_json()
    prod = service.create(data['id'], data['name'], data['price'])
    return jsonify(prod.__dict__), 201