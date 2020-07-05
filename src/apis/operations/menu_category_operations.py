from operations.abstract_operations import Operations
from models.db_models import MenuCategoryDbModel


class MenuCategoryOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        menu_category = MenuCategoryDbModel(**dict(json_obj))
        super()._insert(menu_category)
        return menu_category.id

    def get_all(self):
        return super()._get_all(MenuCategoryDbModel)

    def update(self, json_obj):
        id = json_obj['id']
        if(id is None):
            raise ValueError("id cannot be null or empty")
        del json_obj["id"]
        super()._update(MenuCategoryDbModel, MenuCategoryDbModel.id == id, json_obj)

    def delete(self, id):
        super()._delete(MenuCategoryDbModel, MenuCategoryDbModel.id == id)
