from flask_restful import Resource
from operations import MenuOperations

class MenuController(Resource):

    def __init__(self, *args):
        self.db_operations = args[0]
        self.operations = MenuOperations(self.db_operations)

    def get(self):
        return self.operations.get_complete_menu()