from flask import Blueprint, jsonify, request
from .service import OrderService

order_bp = Blueprint('order', __name__, url_prefix='/orders')
service = OrderService()


@order_bp.route('/', methods=['GET'])
def list_orders():
    orders = service.all()
    return jsonify([o.__dict__ for o in orders])


@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = service.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    return jsonify(order.__dict__)


@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.get_json()
    order = service.create(data['id'], data['user_id'], data.get('product_ids', []))
    return jsonify(order.__dict__), 201