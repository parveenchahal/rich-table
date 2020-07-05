from sqlalchemy import Column, Integer, String, ForeignKey
from models.db_models.db_model import DbModel
from models.db_models.menu_items_db_model import MenuItemsDbModel
from models.db_models.food_type_db_model import FoodTypeDbModel


class MenuByFoodTypeDbModel(DbModel):
    __tablename__ = 'menu_by_food_type'

    id = Column(Integer, primary_key=True)
    food_type_id = Column(Integer, ForeignKey(
        "{0}.id".format(FoodTypeDbModel.__tablename__)))
    menu_item_id = Column(Integer, ForeignKey(
        "{0}.id".format(MenuItemsDbModel.__tablename__)))
