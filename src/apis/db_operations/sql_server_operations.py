from db_operations.abstract_db_operations import DbOperations
class SQLServerOperations(DbOperations):
    def __init__(self, sql_engine):
        self.sql_engine = sql_engine

    def execute_query(self, query):
        with self.sql_engine.connect() as connection:
            result = connection.execute("select name from dbo.menu")
            li = list()
            for row in result:
                li.append({"name":row["name"]})
            return str(li)