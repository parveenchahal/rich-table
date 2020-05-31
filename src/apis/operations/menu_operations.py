from operations.abstract_operations import Operations
from models import MenuModel

class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_string):
        return self.db_operations.insert(MenuModel(**dict(json_string)))

    def get_all(self):
        query_result = self.db_operations.execute("SELECT m.id, m.name, m.category_id, m.price, c.name as type from menu m left join menu_category c on m.category_id = c.id")
        return query_result
