import os
from flask import Flask
from flask_restful import Api, Resource
import config

import config
from sqlalchemy import create_engine
import urllib
from db import db
from operations import Operations, MenuOperations, FoodTypeOperations, MenuCategoryOperations
from controllers import Controller, MenuController, FoodTypeController, MenuCategoryController
from db_operations import SqlServerOperations

app = Flask(__name__)
api = Api(app)

params = "DRIVER={ODBC Driver 17 for SQL Server};%s" % os.environ[
    'RICHTABLE_SQL_CONNECTION_PARAMS']
conn_str = "mssql+pyodbc:///?odbc_connect=%s" % urllib.parse.quote_plus(params)

app.config["SQLALCHEMY_DATABASE_URI"] = conn_str
db.init_app(app)

engine = db.get_engine(app)

db_operations = SqlServerOperations(engine)

menu_operations = MenuOperations(db_operations)
api.add_resource(MenuController, '/apis/menu',
                 resource_class_args=(menu_operations,))

food_type_operations = FoodTypeOperations(db_operations)
api.add_resource(FoodTypeController, '/apis/food_type',
                 resource_class_args=(food_type_operations,))

menu_category_operations = MenuCategoryOperations(db_operations)
api.add_resource(MenuCategoryController, '/apis/menu_category',
                 resource_class_args=(menu_category_operations,))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
