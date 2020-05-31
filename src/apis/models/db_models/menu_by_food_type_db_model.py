from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuByFoodTypeDbModel(Model):

    __tablename__ = 'menu_by_food_type'

    # attributes
    food_type_id: int
    menu_item_id: int
    id: int = None
    