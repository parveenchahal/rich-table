from operations.abstract_operations import Operations
class MenuOperations(Operations):

    def __init__(self, db_operations):
        self.db_operations = db_operations

    def get_complete_menu(self):
        return self.db_operations.execute_query("select name from dbo.menu")