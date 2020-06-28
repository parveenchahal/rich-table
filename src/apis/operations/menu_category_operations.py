from operations.abstract_operations import Operations
from models.db_models import MenuCategoryDbModel

class MenuCategoryOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        menu_category = MenuCategoryDbModel(**dict(json_obj))
        super().insert(menu_category)
        return menu_category.id

    def get_all(self):
        return super().get_all(MenuCategoryDbModel)

    def delete(self, id):
        super().delete(MenuCategoryDbModel, MenuCategoryDbModel.id == id)