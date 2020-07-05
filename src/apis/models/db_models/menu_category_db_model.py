from sqlalchemy import Column, Integer, String
from models.db_models.db_model import DbModel


class MenuCategoryDbModel(DbModel):
    __tablename__ = 'menu_category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
