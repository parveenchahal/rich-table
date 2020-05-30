from flask_restful import Resource
from flask import jsonify

class MenuController(Resource):

    def __init__(self, operations):
        self.operations = operations

    def get(self):
        menus = self.operations.get_all()
        return jsonify([row.__dict__ for row in menus])