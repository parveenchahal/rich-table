from models.abstract_model import BaseModel, Column, Integer, String, Float, ForeignKey

class MenuCategoryModel(BaseModel):
    __tablename__ = 'menu_category'

    id = Column(Integer, primary_key=True)
    name = Column(String)