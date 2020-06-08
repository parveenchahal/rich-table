from sqlalchemy import Column, Integer, String
from models.db_models.db_model import DbModel

class FoodTypeDbModel(DbModel):
    __tablename__ = 'food_type'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_name = Column(String)
