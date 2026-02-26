from flask import Blueprint, jsonify, request
from .service import UserService

user_bp = Blueprint('user', __name__, url_prefix='/users')
service = UserService()


@user_bp.route('/', methods=['GET'])
def list_users():
    users = service.all()
    return jsonify([user.__dict__ for user in users])


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.__dict__)


@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = service.create(data['id'], data['name'], data['email'])
    return jsonify(user.__dict__), 201