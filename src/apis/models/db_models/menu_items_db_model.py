from sqlalchemy import Column, Integer, String, Float
from models.db_models.db_model import DbModel

class MenuItemsDbModel(DbModel):
    __tablename__ = 'menu_items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    image_url = Column(String)
    description = Column(String)
