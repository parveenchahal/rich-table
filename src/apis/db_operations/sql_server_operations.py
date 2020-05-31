from db_operations.abstract_db_operations import DbOperations
class SqlServerOperations(DbOperations):

    def __init__(self, db):
        self.db = db

    @property
    def engine(self):
        return self.db.engine

    def execute_query(self, query):
        with self.engine.connect() as connection:
            query_result = connection.execute(query).fetchall()
            return self.__convert_to_list_of_dict__(query_result)

    def __convert_to_list_of_dict__(self, query_data_rows):
        return ([dict(row) for row in query_data_rows])