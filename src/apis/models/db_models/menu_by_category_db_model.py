from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuByCategoryDbModel(Model):

    __tablename__ = 'menu_by_category'

    # attributes
    menu_category_id: int
    menu_item_id: int
    id: int = None
    