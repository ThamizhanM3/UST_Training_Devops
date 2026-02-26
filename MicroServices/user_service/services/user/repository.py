from typing import List, Optional
from .model import User

# simple in-memory repository
_users: List[User] = []


def add_user(user: User) -> User:
    _users.append(user)
    return user


def get_user(user_id: int) -> Optional[User]:
    return next((u for u in _users if u.id == user_id), None)


def list_users() -> List[User]:
    return list(_users)