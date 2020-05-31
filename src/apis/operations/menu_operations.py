from operations.abstract_operations import Operations
from models import MenuModel, MenuCategoryModel

class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def add_menu(self, json_string):
        MenuModel(kwargs=dict(json_string)).add()

    def get_all(self):
        return (self.db_operations.execute_query("SELECT m.id, m.name, m.category_id, m.price, c.name as type from menu m left join menu_category c on m.category_id = c.id"))
