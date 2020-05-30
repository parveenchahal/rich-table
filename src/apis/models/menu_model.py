from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuModel(Model):
    select_query = "SELECT id, name, product_id, price from menu"

    # attributes
    id: int
    name: str
    product_id: int
    price: float
    