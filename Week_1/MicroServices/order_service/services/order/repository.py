from typing import List, Optional
from .model import Order

_orders: List[Order] = []


def add_order(order: Order) -> Order:
    _orders.append(order)
    return order


def get_order(order_id: int) -> Optional[Order]:
    return next((o for o in _orders if o.id == order_id), None)


def list_orders() -> List[Order]:
    return list(_orders)