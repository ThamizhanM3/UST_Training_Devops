from .repository import add_user, get_user, list_users
from .model import User


class UserService:
    def create(self, user_id: int, name: str, email: str) -> User:
        user = User(id=user_id, name=name, email=email)
        return add_user(user)

    def get(self, user_id: int) -> User:
        return get_user(user_id)

    def all(self):
        return list_users()
