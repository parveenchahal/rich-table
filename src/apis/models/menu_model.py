from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuModel(Model):
    query = "SELECT id, name, product_id, price from menu"

    # attributes
    id: str
    name: int
    product_id: str
    price: float
    