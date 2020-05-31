from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuItemsDbModel(Model):

    __tablename__ = 'menu_items'

    # attributes
    name: str
    price: float
    image_url: str
    description: str
    id: int = None
    