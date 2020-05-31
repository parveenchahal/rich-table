from flask_restful import Resource, reqparse, request, output_json
from flask import jsonify

class MenuController(Resource):

    def __init__(self, operations):
        self.operations = operations

    def get(self):
        menus = self.operations.get_all()
        return output_json(menus, 200, {'Content-Type': 'application/json'})

    def post(self):
        json_data = request.get_json(force=True)
        print(json_data)
        self.operations.insert(json_data)
        return None, 201