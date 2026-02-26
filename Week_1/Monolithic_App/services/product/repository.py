from typing import List, Optional
from .model import Product

_products: List[Product] = []


def add_product(prod: Product) -> Product:
    _products.append(prod)
    return prod


def get_product(prod_id: int) -> Optional[Product]:
    return next((p for p in _products if p.id == prod_id), None)


def list_products() -> List[Product]:
    return list(_products)