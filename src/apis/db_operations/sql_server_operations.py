from db_operations.abstract_db_operations import DbOperations
class SQLServerOperations(DbOperations):
    def query_all(self, model, schema):
        return schema(many=True).dump(model.query.all())