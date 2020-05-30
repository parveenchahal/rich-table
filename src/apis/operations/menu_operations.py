from operations.abstract_operations import Operations
from models import MenuModel

class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def get_all(self):
        query_result = self.db_operations.execute_query(MenuModel.select_query)
        return MenuModel.deserialize(query_result, MenuModel)
