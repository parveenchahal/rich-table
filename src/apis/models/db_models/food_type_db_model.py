from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class FoodTypeDbModel(Model):

    __tablename__ = 'food_type'

    # attributes
    name: str
    short_name: str
    id: int = None
    