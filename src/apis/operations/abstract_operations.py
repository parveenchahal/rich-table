from models.db_models import MenuCategoryDbModel
import abc


class Operations(object):
    def __init__(self, db_operations):
        self.db_operations = db_operations

############ Public methods ###################

    @abc.abstractmethod
    def get(self, id=None):
        raise Exception("Method is not supported.")

    @abc.abstractmethod
    def insert(self, json_obj):
        raise Exception("Method is not supported.")

    @abc.abstractmethod
    def update(self, json_obj):
        raise Exception("Method is not supported.")

    @abc.abstractmethod
    def delete(self, id):
        raise Exception("Method is not supported.")

############ Private methods ##################

    def __create_and_commit_session(self, callback):
        session = self.db_operations.create_session()
        callback(session)
        session.commit()

############ Protected Methods ################

    def _get(self, model, filter_param=None):
        session = self.db_operations.create_session()
        query = session.query(model)
        if(filter_param is not None):
            query = query.filter(filter_param)
        return query.all()

    def _insert(self, model_obj, session=None):
        def insert_callback(session):
            session.add(model_obj)

        if session is None:
            self.__create_and_commit_session(insert_callback)
        else:
            insert_callback(session)

    def _update(self, model, filter_param, json_data, session=None):
        def update_callback(session):
            query_set = session.query(model).filter(filter_param)
            if(query_set.first() is None):
                raise ValueError("id not found")
            query_set.update(json_data)

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
