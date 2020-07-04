from models.db_models import MenuCategoryDbModel

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
        row = session.query(model).filter(filter_param).first()
        if(not row):
            raise KeyError("id not found")
        session.delete(row)
        session.commit()

    def delete_all(self, model, filter_param):
        session = self.db_operations.create_session()
        rows = session.query(model).filter(filter_param).all()
        if(not rows):
            raise KeyError("id not found")
        for row in rows:
            session.delete(row)
        session.commit()
