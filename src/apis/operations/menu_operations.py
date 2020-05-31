from operations.abstract_operations import Operations
from models.db_models import MenuItemsDbModel
from models.view_models import MenuViewModel

class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_string):
        return self.db_operations.insert(MenuItemsDbModel(**dict(json_string)))

    def get_all(self):
        query_result = self.db_operations.execute_query(MenuViewModel.__query__)
        return MenuViewModel.serialize(MenuViewModel.deserialize(query_result, MenuViewModel))
