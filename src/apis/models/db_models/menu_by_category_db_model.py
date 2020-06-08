from sqlalchemy import Column, Integer, String, ForeignKey
from models.db_models.db_model import DbModel
from models.db_models.menu_category_db_model import MenuCategoryDbModel
from models.db_models.menu_items_db_model import MenuItemsDbModel

class MenuByCategoryDbModel(DbModel):
    __tablename__ = 'menu_by_category'
    id = Column(Integer, primary_key=True)
    menu_category_id = Column(Integer, ForeignKey("{0}.id".format(MenuCategoryDbModel.__tablename__)))
    menu_item_id = Column(Integer, ForeignKey("{0}.id".format(MenuItemsDbModel.__tablename__)))
    