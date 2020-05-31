from flask import jsonify
class Operations():
    def __init__(self, db_operations):
        self.db_operations = db_operations