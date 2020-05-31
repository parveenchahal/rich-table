from models.abstract_model import Model
from dataclasses import dataclass

@dataclass
class MenuCategoryDbModel(Model):

    __tablename__ = 'menu_category'

    # attributes
    name: str
    id: int = None
    