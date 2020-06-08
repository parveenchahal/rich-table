from sqlalchemy.orm import sessionmaker
from db_operations.abstract_db_operations import DbOperations

class SqlServerOperations(DbOperations):

    def __init__(self, engine):
        super().__init__(engine)

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def execute_query(self, query):
        with self.engine.connect() as connection:    
            query_result = connection.execute(query).fetchall()
            return query_result