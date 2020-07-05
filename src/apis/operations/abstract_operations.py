from models.db_models import MenuCategoryDbModel


class Operations(object):
    def __init__(self, db_operations):
        self.db_operations = db_operations

############ Private methods ##################

    def __create_and_commit_session(self, callback):
        session = self.db_operations.create_session()
        callback(session)
        session.commit()

############ Protected Methods ##################

    def _insert(self, model_obj, session=None):
        def insert_callback(session):
            session.add(model_obj)

        if session is None:
            self.__create_and_commit_session(insert_callback)
        else:
            insert_callback(session)

    def _get_all(self, model):
        session = self.db_operations.create_session()
        quert_result = session.query(model).all()
        return quert_result

    def _update(self, model_obj, session=None):
        def update_callback(session):
            pass

        if(session is None):
            self.__create_and_commit_session(update_callback)
        else:
            update_callback(session)

    def _delete(self, model, filter_param, session=None):
        def delete_callback(session):
            row = session.query(model).filter(filter_param).first()
            if(not row):
                raise KeyError("id not found")
            session.delete(row)

        if(session is None):
            self.__create_and_commit_session(delete_callback)
        else:
            delete_callback(session)

    def _delete_all(self, model, filter_param, session=None):
        def delete_all_callback(session):
            rows = session.query(model).filter(filter_param).all()
            if(not rows):
                raise KeyError("id not found")
            for row in rows:
                session.delete(row)

        if(session is None):
            self.__create_and_commit_session(delete_all_callback)
        else:
            delete_all_callback(session)
