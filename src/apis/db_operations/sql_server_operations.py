from db_operations.abstract_db_operations import DbOperations
class SqlServerOperations(DbOperations):

    def __init__(self, engine):
        super().__init__(engine)
        pass

    def execute_query(self, query):
        query_result = self.execute.fetchall()
        return self.__convert_to_list_of_dict__(query_result)

    def insert(self, model_obj):
        keys_list = list()
        values_list = list()
        for key in model_obj.__dict__:
            if(model_obj.__dict__[key] is not None):
                keys_list.append(key)
                values_list.append(model_obj.__dict__[key])
        if(len(keys_list) is 0):
            raise ValueError()
        keys_str = str(keys_list)
        keys_str = keys_str.replace("'", "")
        keys_str = SqlServerOperations.__stringify_list__(keys_str)
        values_str = str(values_list)
        values_str = SqlServerOperations.__stringify_list__(values_str)
        statement = "INSERT INTO {0} {1} VALUES{2}".format(model_obj.__tablename__, keys_str, values_str)
        self.execute(statement)

    @staticmethod
    def __stringify_list__(lis):
        if len(lis) is not 0:
            s = str(lis)
            return "({0})".format(s[1:-1])
        return "()"

    def execute(self, statement):
        with self.engine.connect() as connection:
            return connection.execute(statement)

    def __convert_to_list_of_dict__(self, query_data_rows):
        return ([dict(row) for row in query_data_rows])