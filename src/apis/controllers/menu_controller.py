from flask_restful import Resource
from flask import jsonify

class MenuController(Resource):

    def __init__(self, operations):
        self.operations = operations

    def get(self):
        menus = self.operations.get_all()
        return jsonify(menus)
    
    def post(self):
        menus = self.operations.get_all()
        return jsonify(menus)