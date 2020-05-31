from models.abstract_model import BaseModel, Column, Integer, String, Float, ForeignKey

class MenuModel(BaseModel):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("menu_category.id"))
    price = Column(Float)