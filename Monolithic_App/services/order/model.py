from dataclasses import dataclass
from typing import List

@dataclass
class Order:
    id: int
    user_id: int
    product_ids: List[int]
