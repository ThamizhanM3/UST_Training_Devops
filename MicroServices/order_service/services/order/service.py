from .repository import add_order, get_order, list_orders
from .model import Order


class OrderService:
    def create(self, order_id: int, user_id: int, product_ids: list[int]) -> Order:
        order = Order(id=order_id, user_id=user_id, product_ids=product_ids)
        return add_order(order)

    def get(self, order_id: int) -> Order:
        return get_order(order_id)

    def all(self):
        return list_orders()