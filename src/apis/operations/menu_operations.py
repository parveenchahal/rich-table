from operations.abstract_operations import Operations
from flask_marshmallow import Marshmallow
from models import MenuModel, MenuSchema

class MenuOperations(Operations):

    def __init__(self, db_operations):
        self.db_operations = db_operations

    def get_complete_menu(self):
        return self.db_operations.query_all(MenuModel, MenuSchema)