from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuViewModel(Model):
    __query__ = 'SELECT m.id, m.name, m.price, c.name as category from menu m left join menu_category c on m.category_id = c.id'

    id: int
    name: str
    category: str
    price: float
