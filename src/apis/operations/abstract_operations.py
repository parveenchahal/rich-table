class Operations(object):
    def __init__(self, db_operations):
        self.db_operations = db_operations

    def insert(self, model_obj):
        session = self.db_operations.create_session()
        session.add(model_obj)
        session.commit()

    def get_all(self, model):
        session = self.db_operations.create_session()
        quert_result = session.query(model).all()
        return quert_result

    def delete(self, model, filter_param):
        session = self.db_operations.create_session()
        row = session.query(model).filter(filter_param)
        if(row):
            raise str(row)
        row.delete()
        session.commit()
