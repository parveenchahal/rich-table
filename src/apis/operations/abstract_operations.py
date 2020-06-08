class Operations(object):
    def __init__(self, db_operations):
        self.db_operations = db_operations

    def insert(self, json_string):
        raise NotImplementedError()

    def get_all(self):
        raise NotImplementedError()
