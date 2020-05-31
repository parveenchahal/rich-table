from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuModel(Model):

    __tablename__ = 'menu'

    # attributes
    name: str
    category_id: int
    price: float
    id: int = None
    