from .repository import add_product, get_product, list_products
from .model import Product


class ProductService:
    def create(self, prod_id: int, name: str, price: float) -> Product:
        prod = Product(id=prod_id, name=name, price=price)
        return add_product(prod)

    def get(self, prod_id: int) -> Product:
        return get_product(prod_id)

    def all(self):
        return list_products()